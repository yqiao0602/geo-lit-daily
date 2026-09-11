#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""geo-lit-daily：arXiv + OpenAlex 每日文献采集 → 关键词粗筛 → LLM 打分/总结/课题关联 → 日报 → 邮件/微信推送"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from email.header import Header
from email.mime.text import MIMEText

import smtplib

import yaml

BASE = os.path.dirname(os.path.abspath(__file__))
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ('utf-8', 'utf8'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

with open(os.path.join(BASE, 'config.yaml'), encoding='utf-8') as f:
    CFG = yaml.safe_load(f)


def http_get(url, timeout=45, retries=4):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': f'geo-lit-daily ({CFG["mailto"]})'})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode('utf-8', errors='ignore')
        except urllib.error.HTTPError as e:
            last = e
            if e.code == 429:
                time.sleep(20 * (i + 1))
                continue
            if e.code >= 500:
                time.sleep(6 * (i + 1))
                continue
            raise
        except Exception as e:
            last = e
            time.sleep(6 * (i + 1))
    raise last


def http_post_json(url, payload, headers, timeout=120):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, method='POST',
                                 headers={**headers, 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


# ---------------- arXiv ----------------

def fetch_arxiv(since=None):
    ns = {'a': 'http://www.w3.org/2005/Atom'}

    def parse(xml_text):
        root = ET.fromstring(xml_text)
        out = []
        for e in root.findall('a:entry', ns):
            raw = e.find('a:id', ns).text or ''
            m = re.search(r'abs/(.+)', raw)
            aid = m.group(1) if m else raw
            out.append({
                'id': 'arxiv:' + re.sub(r'v\d+$', '', aid),
                'title': ' '.join((e.find('a:title', ns).text or '').split()),
                'abstract': ' '.join((e.find('a:summary', ns).text or '').split()),
                'authors': [a.find('a:name', ns).text for a in e.findall('a:author', ns)][:6],
                'venue': 'arXiv',
                'url': f'https://arxiv.org/abs/{aid}',
                'pdf': f'https://arxiv.org/pdf/{aid}',
                'date': (e.find('a:published', ns).text or '')[:10],
            })
        return out

    papers = []
    page = 100
    until = date.today()
    if since is None:
        cats = CFG['arxiv']['categories']
        d0 = date.today() - timedelta(days=CFG['arxiv']['window_days'])
        cat_q = '(' + ' OR '.join(f'cat:{c}' for c in cats) + ')'
        queries = [f'{cat_q} AND submittedDate:[{d0:%Y%m%d}0000 TO {until:%Y%m%d}2359]']
        max_each = CFG['arxiv']['max_results']
    else:
        queries = [f'all:"{p}" AND submittedDate:[{since:%Y%m%d}0000 TO {until:%Y%m%d}2359]'
                   for p in CFG['openalex']['search_queries']]
        max_each = 150
    for q in queries:
        qe = urllib.parse.quote(q)
        for start in range(0, max_each, page):
            url = (f'https://export.arxiv.org/api/query?search_query={qe}'
                   f'&sortBy=submittedDate&sortOrder=descending&start={start}&max_results={page}')
            try:
                chunk = parse(http_get(url, timeout=90))
            except Exception as e:
                print(f'  [warn] arXiv 拉取失败: {str(e)[:90]}')
                if not papers and len(queries) == 1:
                    raise
                break
            papers += chunk
            if len(chunk) < page:
                break
            time.sleep(3)   # arXiv API 官方要求请求间隔 ≥3s
        if len(queries) > 1:
            time.sleep(3)
    return papers


# ---------------- OpenAlex ----------------

def reconstruct_abstract(inv):
    if not inv:
        return ''
    pos = {}
    for word, places in inv.items():
        for p in places:
            pos[p] = word
    return ' '.join(pos[i] for i in sorted(pos))


def fetch_openalex(since=None):
    oa = CFG['openalex']
    daily = since is None
    if daily:
        d0 = date.today() - timedelta(days=oa['window_days'])
        author_pages, search_pages = 1, 1
    else:
        d0 = since
        author_pages, search_pages = 2, 3
    datef = f'from_publication_date:{d0:%Y-%m-%d}'
    select = '&select=id,doi,title,publication_date,authorships,primary_location,abstract_inverted_index,ids'
    base = f'https://api.openalex.org/works?mailto={urllib.parse.quote(CFG["mailto"])}'

    urls = []
    if daily:
        jids = [j['id'] for j in oa['journals']]
        if jids:
            urls.append((f'期刊×{len(jids)}',
                         f'{base}&per-page=50&sort=publication_date:desc'
                         f'&filter={datef},primary_location.source.id:{"|".join(jids)}{select}', 1))
    aids = [a['id'] for a in oa['authors']]
    if aids:
        urls.append((f'作者×{len(aids)}',
                     f'{base}&per-page=50&sort=publication_date:desc'
                     f'&filter={datef},author.id:{"|".join(aids)}{select}', author_pages))
    for q in oa.get('search_queries', []):
        urls.append((f'检索:{q}',
                     f'{base}&per-page=50&sort=relevance_score:desc'
                     f'&filter={datef},default.search:{urllib.parse.quote(q)}{select}', search_pages))

    name_by_id = {a['id']: a['name'] for a in oa['authors']}
    papers, seen = [], set()

    def absorb(results):
        for w in results:
            try:
                wid = (w.get('id') or '')
                if not wid:
                    continue
                wid = wid.split('/')[-1]
                if wid in seen:
                    continue
                seen.add(wid)
                ax = (w.get('ids') or {}).get('arxiv') or ''
                pid = 'arxiv:' + ax.rsplit('/', 1)[-1] if ax else 'oa:' + wid
                auth_ids = {(a['author'].get('id') or '').split('/')[-1]
                            for a in w.get('authorships', []) if a.get('author')}
                hit = [n for i in auth_ids if (n := name_by_id.get(i))]
                papers.append({
                    'id': pid,
                    'title': w.get('title') or '(无题)',
                    'abstract': reconstruct_abstract(w.get('abstract_inverted_index')),
                    'authors': [a['author'].get('display_name', '?') for a in w.get('authorships', [])][:6],
                    'venue': ((w.get('primary_location') or {}).get('source') or {}).get('display_name') or '预印本',
                    'url': w.get('doi') or f'https://openalex.org/{wid}',
                    'date': w.get('publication_date') or '',
                    'author_hit': hit,
                })
            except Exception as e:
                print(f'  [warn] 解析单条记录失败: {e}')

    for label, url, max_pages in urls:
        for page in range(1, max_pages + 1):
            try:
                data = json.loads(http_get(f'{url}&page={page}'))
            except Exception as e:
                print(f'  [warn] OpenAlex {label} 第{page}页失败: {e}')
                break
            absorb(data.get('results', []))
            time.sleep(1.5)
            if len(data.get('results', [])) < 50:
                break
    return papers


# ---------------- 关键词粗筛 ----------------

def make_matcher(term):
    if len(term) <= 4 and re.fullmatch(r'[a-z0-9\-]+', term):
        return re.compile(r'\b' + re.escape(term) + r'\b', re.I)
    return re.compile(re.escape(term), re.I)


def kw_filter(papers):
    D = [make_matcher(t) for t in CFG['filter']['domain_terms']]
    T = [make_matcher(t) for t in CFG['filter']['task_terms']]
    S = [make_matcher(t) for t in CFG['filter']['strong_terms']]
    kept = []
    for p in papers:
        if p.get('author_hit'):
            p['why'] = '作者跟踪: ' + ', '.join(p['author_hit'])
            kept.append(p)
            continue
        text = (p['title'] + ' ' + p['abstract']).lower()
        if any(r.search(text) for r in S):
            p['why'] = '强命中'
            kept.append(p)
            continue
        if any(r.search(text) for r in D) and any(r.search(text) for r in T):
            p['why'] = '领域×任务'
            kept.append(p)
    return kept


# ---------------- LLM ----------------

def llm_annotate(papers):
    key = os.environ.get('LIT_LLM_API_KEY', '')
    base = os.environ.get('LIT_LLM_BASE_URL', CFG['llm'].get('base_url', ''))
    model = os.environ.get('LIT_LLM_MODEL', CFG['llm'].get('model', ''))
    if not (key and base and model):
        print('[info] 未配置 LIT_LLM_API_KEY，跳过 LLM 打分（仅关键词粗筛）')
        return papers, '未启用（未配置 LLM Secret）'
    if not papers:
        return papers, '无候选'
    sys_prompt = (
        '你是科研文献筛选助手。我的研究方向如下：\n' + CFG['profile'].strip() + '\n\n'
        '下面给你一篇论文的标题与摘要，请只输出一个 JSON 对象，不要输出任何其他文字：\n'
        '{"score": 0到10的整数(与课题相关性), "one_line": "一句话概括论文做了什么(中文)", '
        '"summary": "2-3句中文总结(痛点/方法/结果)", '
        '"connection": "与我的课题的具体联系，指明相关模块(如M1架构/M2领域预训练/M3微调/KG约束/landing/评测/数据/可对比基线)；若无关就写\\"无关\\"", '
        '"inspiration": "这篇论文能给课题带来的新启发或可直接偷的具体做法(1-2句)；没有则写\\"无\\"", '
        '"limitation": "论文自身局限或引用时注意点(1句)", '
        '"action": "精读|对比基线|引用|略读|忽略 之一", '
        '"tag": "M1|M2|M3|KG|landing|eval|data|baseline|综述|无关 之一"}'
    )
    ok = 0
    for p in papers:
        user = (f'标题: {p["title"]}\n作者: {", ".join(p["authors"])}\n'
                f'来源: {p["venue"]} ({p["date"]})\n摘要: {p["abstract"][:1500]}')
        try:
            r = http_post_json(
                base.rstrip('/') + '/chat/completions',
                {'model': model, 'temperature': 0.2,
                 'messages': [{'role': 'system', 'content': sys_prompt},
                              {'role': 'user', 'content': user}]},
                {'Authorization': 'Bearer ' + key})
            txt = r['choices'][0]['message']['content']
            m = re.search(r'\{.*\}', txt, re.S)
            d = json.loads(m.group(0)) if m else {}
            p['score'] = int(d.get('score') or 0)
            p['one_line'] = d.get('one_line', '')
            p['summary'] = d.get('summary', '')
            p['connection'] = d.get('connection', '')
            p['inspiration'] = d.get('inspiration', '')
            p['limitation'] = d.get('limitation', '')
            p['action'] = d.get('action', '')
            p['tag'] = d.get('tag', '')
            ok += 1
        except Exception as e:
            print(f'  [warn] LLM 调用失败: {p["title"][:50]} | {e}')
            p['score'] = None
        time.sleep(0.6)
    status = f'正常（{ok}/{len(papers)} 篇完成打分）' if ok else '调用失败（检查 key / base_url / model）'
    return papers, status


def llm_editorial(hit):
    key = os.environ.get('LIT_LLM_API_KEY', '')
    base = os.environ.get('LIT_LLM_BASE_URL', CFG['llm'].get('base_url', ''))
    model = os.environ.get('LIT_LLM_MODEL', CFG['llm'].get('model', ''))
    if not (key and base and model and hit):
        return ''
    listing = '\n'.join(f'- [{p.get("score")}] {p["title"]}：{p.get("one_line", "")}' for p in hit)
    sys_p = ('你是文献日报主编。以下是今日命中论文列表。用 2-3 句中文写一段"今日速览"导语：'
             '今天整体风向是什么、最该先看哪 1-2 篇、与课题的紧迫关联（竞品动向/可借的东风）。'
             '直接输出导语正文，不要标题、不要客套、不要列表。')
    try:
        r = http_post_json(
            base.rstrip('/') + '/chat/completions',
            {'model': model, 'temperature': 0.4,
             'messages': [{'role': 'system', 'content': sys_p},
                          {'role': 'user', 'content': listing}]},
            {'Authorization': 'Bearer ' + key})
        return r['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f'  [warn] 导语生成失败: {e}')
        return ''


# ---------------- 渲染 ----------------

def pick(kept):
    hit = [p for p in kept if p.get('score') is None or p.get('score', 0) >= CFG['min_score']]
    hit.sort(key=lambda p: p.get('score') or 0, reverse=True)
    return hit[:CFG['max_papers']]


GROUPS = [('baseline', '🎯 直接竞品与对比基线'),
          ('M1', '🧩 M1 · 自研架构'),
          ('M2', '🎓 M2 · 领域继续预训练与后训练'),
          ('M3', '⚡ M3 · 任务级微调'),
          ('KG', '🕸️ 知识图谱与约束'),
          ('landing', '🛬 Landing 与工具落地'),
          ('eval', '📏 评测与基准'),
          ('data', '📦 数据与语料'),
          ('综述', '📚 综述与立场'),
          (None, '🧷 其他')]


def _links_md(p):
    s = f'[原文]({p["url"]})'
    if p.get('pdf'):
        s += f' · [PDF]({p["pdf"]})'
    return s


def _card_md(p):
    s = p.get('score')
    stars = '⭐' * max(1, round((s or 5) / 2)) if s is not None else '▫️'
    lines = [f'### {stars} {p["title"]}',
             f'**{s if s is not None else "-"}/10** · {"、".join(p["authors"])} · {p["venue"]} · {p["date"]} · {_links_md(p)}']
    if p.get('why'):
        lines.append(f'*入选：{p["why"]}*')
    if p.get('one_line'):
        lines.append(f'\n**一句话**：{p["one_line"]}')
    if p.get('summary'):
        lines.append(f'\n{p["summary"]}')
    if p.get('connection'):
        lines.append(f'\n> 🔗 **与课题**：{p["connection"]}')
    if p.get('inspiration'):
        lines.append(f'\n💡 **启发**：{p["inspiration"]}')
    if p.get('limitation'):
        lines.append(f'\n⚠️ **局限**：{p["limitation"]}')
    if p.get('action'):
        lines.append(f'\n**▸ 建议：{p["action"]}**')
    lines.append('')
    return lines


def render_md(hit, today, total_fetched, total_fresh, llm_status='未知', editorial=''):
    lines = [f'# 📚 文献日报 {today}', '',
             f'> 采集 {total_fresh} 篇（昨日窗口共 {total_fetched} 条）→ 收录 {len(hit)} 篇'
             f'｜阈值 {CFG["min_score"]}/10｜上限 {CFG["max_papers"]} 篇',
             f'> AI 总结：**{llm_status}**', '']
    if editorial:
        lines += [f'**📮 今日速览**：{editorial}', '']
    if not hit:
        lines.append('今天没有命中文献。')
    grouped = {}
    for p in hit:
        tag = p.get('tag') if p.get('tag') in {g[0] for g in GROUPS if g[0]} else None
        grouped.setdefault(tag, []).append(p)
    for tag, title in GROUPS:
        grp = grouped.get(tag)
        if not grp:
            continue
        grp.sort(key=lambda p: p.get('score') or 0, reverse=True)
        lines.append(f'## {title}（{len(grp)} 篇）')
        lines.append('')
        for p in grp:
            lines += _card_md(p)
    lines.append('---\n*geo-lit-daily 自动生成 · 画像与阈值见 config.yaml*')
    return '\n'.join(lines)


def _card_html(p):
    s = p.get('score', '?')
    pdf = f' · <a href="{p["pdf"]}">PDF</a>' if p.get('pdf') else ''
    rows = (f'<h3 style="margin:0 0 6px"><a href="{p["url"]}">{p["title"]}</a></h3>'
            f'<div style="color:#888;font-size:12px">{s}/10 · {"、".join(p["authors"])} · {p["venue"]} · {p["date"]}'
            f' · <a href="{p["url"]}">原文</a>{pdf}</div>')
    if p.get('one_line'):
        rows += f'<p style="font-size:13px"><b>一句话：</b>{p["one_line"]}</p>'
    if p.get('summary'):
        rows += f'<p style="font-size:13px">{p["summary"]}</p>'
    if p.get('connection'):
        rows += (f'<p style="font-size:13px;background:#eef5ff;padding:8px;border-radius:6px">'
                 f'<b>🔗 与课题：</b>{p["connection"]}</p>')
    if p.get('inspiration'):
        rows += (f'<p style="font-size:13px;background:#f3f0ff;padding:8px;border-radius:6px">'
                 f'<b>💡 启发：</b>{p["inspiration"]}</p>')
    if p.get('limitation'):
        rows += f'<p style="font-size:12px;color:#a06000">⚠️ {p["limitation"]}</p>'
    if p.get('action'):
        rows += f'<p style="font-size:13px"><b>▸ 建议：{p["action"]}</b></p>'
    return (f'<div style="border:1px solid #ddd;border-radius:8px;padding:12px;margin:12px 0;'
            f'font-family:sans-serif;max-width:720px">{rows}</div>')


def render_html(hit, today, llm_status='未知', editorial=''):
    good = llm_status.startswith('正常')
    color = '#2e7d32' if good else '#e65100'
    bg = '#e8f5e9' if good else '#fff3e0'
    out = (f'<h2>📚 文献日报 {today}（{len(hit)} 篇）</h2>'
           f'<div style="padding:8px 12px;border-radius:6px;background:{bg};color:{color};'
           f'font-size:13px;font-family:sans-serif;margin:8px 0;max-width:720px">'
           f'<b>AI 总结：{llm_status}</b></div>')
    if editorial:
        out += (f'<div style="background:#f5f0ff;border-left:4px solid #7c4dff;padding:10px 14px;'
                f'font-size:14px;font-family:sans-serif;margin:10px 0;max-width:720px">'
                f'<b>📮 今日速览</b><br>{editorial}</div>')
    grouped = {}
    for p in hit:
        tag = p.get('tag') if p.get('tag') in {g[0] for g in GROUPS if g[0]} else None
        grouped.setdefault(tag, []).append(p)
    for tag, title in GROUPS:
        grp = grouped.get(tag)
        if not grp:
            continue
        grp.sort(key=lambda p: p.get('score') or 0, reverse=True)
        out += f'<h2 style="font-size:16px">{title}（{len(grp)} 篇）</h2>'
        out += ''.join(_card_html(p) for p in grp)
    return out


def render_backlog(hit, since, n_cand, n_scored, llm_status):
    def block(p):
        s = p.get('score') or 0
        lines = [f'### {"⭐" * max(1, round(s / 2))} {p["title"]}',
                 f'**{s}/10** · {"、".join(p["authors"])} · {p["venue"]} · {p["date"]} · [原文]({p["url"]})']
        if p.get('why'):
            lines.append(f'*来源：{p["why"]}*')
        if p.get('one_line'):
            lines.append(f'\n**一句话**：{p["one_line"]}')
        if p.get('summary'):
            lines.append(f'\n{p["summary"]}')
        if p.get('connection'):
            lines.append(f'\n> 🔗 **与课题**：{p["connection"]}')
        return '\n'.join(lines)

    out = [f'# 📚 存量文献清单（backlog）— 扫描自 {since:%Y-%m-%d}', '',
           f'> 候选 {n_cand} 篇 → LLM 打分 {n_scored} 篇 → 收录 {len(hit)} 篇'
           f'｜阈值 {CFG["min_score"]}/10｜AI 总结：{llm_status}', '']
    bands = [(8, '🔥 8 分以上：直接相关'),
             (6, '👀 6-7 分：值得一看'),
             (CFG['min_score'], f'📎 {CFG["min_score"]}-5 分：备查')]
    covered = 11
    for lo, title in bands:
        grp = [p for p in hit if lo <= (p.get('score') or 0) < covered]
        covered = lo
        if grp:
            out += [f'## {title}（{len(grp)} 篇）', '']
            out += [block(p) + '\n' for p in grp]
    return '\n'.join(out)


def backfill(since):
    print(f'=== geo-lit-daily BACKLOG 自 {since:%Y-%m-%d} ===')
    papers = []
    try:
        ax = fetch_arxiv(since)
        print(f'[arXiv 检索式] {len(ax)} 篇')
        papers += ax
    except Exception as e:
        print(f'[warn] arXiv 失败: {e}')
    try:
        oa = fetch_openalex(since)
        print(f'[OpenAlex 作者+检索] {len(oa)} 篇')
        papers += oa
    except Exception as e:
        print(f'[warn] OpenAlex 失败: {e}')
    seen_titles, uniq = set(), []
    for p in papers:
        t = re.sub(r'\W', '', p['title'].lower())[:80]
        if t and t in seen_titles:
            continue
        seen_titles.add(t)
        uniq.append(p)
    kept = kw_filter(uniq)
    print(f'[粗筛] {len(uniq)} -> {len(kept)}')
    cap = int(CFG.get('backfill', {}).get('max_llm', 400))
    if len(kept) > cap:
        kept.sort(key=lambda p: 0 if p.get('author_hit') else 1)
        print(f'[截断] {len(kept)} 超出 LLM 上限 {cap}，作者跟踪优先，截去 {len(kept) - cap} 篇')
        kept = kept[:cap]
    kept, llm_status = llm_annotate(kept)
    scored = sorted((p['score'] for p in kept if p.get('score') is not None), reverse=True)
    if scored:
        print(f'[LLM] {llm_status} | 全部分数(降序): {scored[:15]}')
    hit = [p for p in kept if (p.get('score') or 0) >= CFG['min_score']]
    hit.sort(key=lambda p: ((p.get('score') or 0), p.get('date') or ''), reverse=True)
    md = render_backlog(hit, since, len(uniq), len(kept), llm_status)
    with open(os.path.join(BASE, 'backlog.md'), 'w', encoding='utf-8') as f:
        f.write(md)
    print(f'[ok] backlog.md：收录 {len(hit)} 篇（AI 总结 {llm_status}）')


# ---------------- 推送 ----------------

def push_email(subject, html):
    host = os.environ.get('LIT_SMTP_HOST', CFG['email']['host'])
    port = int(os.environ.get('LIT_SMTP_PORT', str(CFG['email']['port'])))
    user = os.environ.get('LIT_SMTP_USER', '')
    pwd = os.environ.get('LIT_SMTP_PASS', '')
    to = os.environ.get('LIT_TO_EMAIL', '')
    if not all([user, pwd, to]):
        print('[info] 邮件未配置，跳过')
        return
    msg = MIMEText(html, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = user
    msg['To'] = to
    smtp = smtplib.SMTP_SSL(host, port) if port == 465 else smtplib.SMTP(host, port)
    try:
        if port != 465:
            smtp.starttls()
        smtp.login(user, pwd)
        smtp.sendmail(user, [to], msg.as_string())
        print(f'[ok] 邮件已发送 -> {to}')
    finally:
        smtp.quit()


def push_wechat(title, md):
    key = os.environ.get('LIT_SERVERCHAN_KEY', '')
    if not key:
        print('[info] Server酱未配置，跳过')
        return
    data = urllib.parse.urlencode({'title': title[:32], 'desp': md[:28000]}).encode()
    req = urllib.request.Request(f'https://sctapi.ftqq.com/{key}.send', data=data)
    with urllib.request.urlopen(req, timeout=30) as r:
        print('[ok] Server酱:', json.loads(r.read().decode()).get('message'))


# ---------------- 状态 ----------------

STATE_FILE = os.path.join(BASE, 'state.json')


def load_state():
    if os.path.exists(STATE_FILE):
        try:
            return json.load(open(STATE_FILE, encoding='utf-8'))
        except Exception:
            pass
    return {'seen': {}}


def save_state(state):
    cutoff = (date.today() - timedelta(days=90)).isoformat()
    state['seen'] = {k: v for k, v in state['seen'].items() if v >= cutoff}
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=0)


def main():
    dry = '--dry-run' in sys.argv
    today = date.today().isoformat()
    print(f'=== geo-lit-daily {today} {"(dry-run)" if dry else ""} ===')

    papers = []
    try:
        ax = fetch_arxiv()
        print(f'[arXiv] 4 类目 {CFG["arxiv"]["window_days"]} 天: {len(ax)} 篇')
        papers += ax
    except Exception as e:
        print(f'[warn] arXiv 拉取失败: {e}')
    try:
        oa = fetch_openalex()
        print(f'[OpenAlex] 期刊+作者+检索: {len(oa)} 篇')
        papers += oa
    except Exception as e:
        print(f'[warn] OpenAlex 拉取失败: {e}')
    if not papers:
        print('[error] 两个数据源均失败，退出')
        sys.exit(1)

    # 标题级去重（跨源同一篇）
    seen_titles, uniq = set(), []
    for p in papers:
        t = re.sub(r'\W', '', p['title'].lower())[:80]
        if t and t in seen_titles:
            continue
        seen_titles.add(t)
        uniq.append(p)
    papers = uniq

    state = load_state()
    fresh = [p for p in papers if p['id'] not in state['seen']]
    print(f'[去重] {len(papers)} -> 新增 {len(fresh)}')

    kept = kw_filter(fresh)
    print(f'[粗筛] {len(fresh)} -> {len(kept)}')

    kept, llm_status = llm_annotate(kept)
    scored = sorted((p['score'] for p in kept if p.get('score') is not None), reverse=True)
    if scored:
        print(f'[LLM] {llm_status} | 全部分数(降序): {scored[:15]}')
    hit = pick(kept)
    print(f'[收录] {len(hit)} 篇')

    editorial = llm_editorial(hit) if hit else ''
    md = render_md(hit, today, len(papers), len(fresh), llm_status, editorial)
    os.makedirs(os.path.join(BASE, 'daily'), exist_ok=True)
    out = os.path.join(BASE, 'daily', today + '.md')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f'[ok] 日报: {out}')

    if not dry:
        for p in papers:
            state['seen'][p['id']] = today
        save_state(state)
        if hit:
            subj = f'📚 文献日报 {today}: {len(hit)} 篇命中'
            if not llm_status.startswith('正常'):
                subj += f'（AI总结{llm_status[:6]}…）'
            push_email(subj, render_html(hit, today, llm_status, editorial))
            push_wechat(f'文献日报 {today}: {len(hit)}篇', md)
        else:
            print('[info] 今日无命中，不推送')
    else:
        print('[dry-run] 不更新 state.json、不推送')


if __name__ == '__main__':
    if '--backfill' in sys.argv:
        i = sys.argv.index('--backfill')
        arg = sys.argv[i + 1] if len(sys.argv) > i + 1 else '2024'
        backfill(date(int(arg), 1, 1) if arg.isdigit() else date(2024, 1, 1))
    else:
        main()
