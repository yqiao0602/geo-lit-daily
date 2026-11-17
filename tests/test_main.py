import json
import os
import urllib.error
import unittest
from unittest import mock

import main


class PipelineTests(unittest.TestCase):
    def test_s2_record_prefers_doi_and_maps_fields(self):
        record = main._s2_record({
            'paperId': 'p1', 'title': 'A paper', 'abstract': 'Abstract',
            'authors': [{'name': 'Alice'}], 'venue': 'Venue',
            'publicationDate': '2026-01-02',
            'url': 'https://example.test/p1',
            'openAccessPdf': {'url': 'https://example.test/p1.pdf'},
            'externalIds': {'DOI': '10.123/ABC'},
        }, ['Alice'])
        self.assertEqual(record['id'], 'doi:10.123/abc')
        self.assertEqual(record['abstract'], 'Abstract')
        self.assertTrue(record['pdf'].endswith('.pdf'))
        self.assertEqual(record['author_hit'], ['Alice'])

    def test_s2_get_passes_api_key_and_waits_before_each_attempt(self):
        responses = [urllib.error.HTTPError(
            'https://example.test', 429, 'limited', {'Retry-After': '0'}, None),
            mock.Mock(read=lambda: b'{"ok": true}', __enter__=lambda self: self,
                      __exit__=lambda *args: None)]
        with mock.patch.object(main._S2_LIMITER, 'wait') as wait, \
             mock.patch('main.urllib.request.urlopen', side_effect=responses) as opener:
            self.assertTrue(json.loads(main._s2_get(
                'https://example.test', {'x-api-key': 'secret'}))['ok'])
        self.assertEqual(wait.call_count, 2)
        self.assertEqual(opener.call_args_list[0].args[0].headers['X-api-key'], 'secret')

    def test_openalex_key_is_optional_and_url_encoded(self):
        captured = []
        with mock.patch.dict(os.environ, {'LIT_OPENALEX_API_KEY': 'a/b'}, clear=False), \
             mock.patch('main.http_get', side_effect=lambda url, **kwargs: captured.append(url) or '{"results": []}'):
            main.fetch_openalex()
        self.assertIn('api_key=a%2Fb', captured[0])

    def test_s2_missing_key_skips_network(self):
        with mock.patch.dict(os.environ, {}, clear=True), \
             mock.patch('main._s2_get') as get:
            self.assertEqual(main.fetch_semantic_scholar(), [])
        get.assert_not_called()


if __name__ == '__main__':
    unittest.main()
