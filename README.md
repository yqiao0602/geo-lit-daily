# geo-lit-daily 每日文献订阅推送

针对课题「自然语言 → 工作流自动构建」的私人文献日报系统。

**数据源**：arXiv（cs.AI/CL/LG/SE 预印本）+ OpenAlex（12 本 GIS 期刊 + 12 位跟踪作者 + 关键词全库检索）
**流程**：采集 → 关键词粗筛 → LLM 打分/中文总结/课题关联 → markdown 日报 → 邮件 + Server酱微信
**运行**：GitHub Actions 每天北京时间 07:30 自动执行，日报归档在 `daily/` 目录

与现成项目（zotero-arxiv-daily 等）的区别：补齐期刊源、注入研究画像、每篇附"与课题的具体联系"。

## 本地测试

```bash
pip install -r requirements.txt
python main.py --dry-run     # 不推送、不写 state.json，产出 daily/当日.md
```

## 部署到 GitHub Actions（一次性）

1. 在 GitHub 上新建空仓库（如 `geo-lit-daily`，私有即可）
2. 本地推送：

```bash
cd E:/02_projects/03_PythonProject/geo-lit-daily
git init
git add .
git commit -m "init"
git remote add origin https://github.com/<你的用户名>/geo-lit-daily.git
git push -u origin main
```

3. 仓库 → Settings → Secrets and variables → Actions → New repository secret，逐个添加：

| Secret 名 | 值 | 说明 |
|---|---|---|
| `LIT_LLM_API_KEY` | sk-xxx | LLM 密钥（DeepSeek/GLM/Qwen 等任意 OpenAI 兼容服务） |
| `LIT_LLM_BASE_URL` | `https://api.deepseek.com` | 与密钥配套的接口地址（DeepSeek 带不带 `/v1` 均可） |
| `LIT_LLM_MODEL` | `deepseek-flash` | 模型名（2026-09 DeepSeek 在售：deepseek-flash；GLM 示例：glm-4.6） |
| `LIT_SMTP_HOST` | `smtp.qq.com` | 发件邮箱 SMTP（QQ/163 均可） |
| `LIT_SMTP_PORT` | `465` | QQ/163 用 465 |
| `LIT_SMTP_USER` | xxx@qq.com | 发件邮箱地址 |
| `LIT_SMTP_PASS` | （授权码） | QQ邮箱→设置→账户→开启SMTP→生成授权码 |
| `LIT_TO_EMAIL` | xxx@qq.com | 收件邮箱（可以和发件相同） |
| `LIT_SERVERCHAN_KEY` | SCTxxxx | [sct.ftqq.com](https://sct.ftqq.com) 微信扫码登录后复制 SendKey；不需要微信推送可不配 |

4. 仓库 → Actions → daily → Enable workflow；可先点 Run workflow 手动跑一次验证
5. 之后每天北京时间约 07:30 自动推送，`daily/` 目录自动归档

## 日常调整（都在 config.yaml）

- **研究画像**：`profile` 字段，直接改中文描述，LLM 打分和"与课题联系"随之变化
- **加减期刊**：`openalex.journals`（去 [openalex.org](https://openalex.org) 搜期刊名拿 source id）
- **加减作者**：`openalex.authors`（OpenAlex 搜作者名拿 author id；重名多，务必核对单位）
- **收录量**：`min_score`（阈值）、`max_papers`（上限）
- **粗筛词表**：`filter` 三组词（strong 任一命中即收；domain+task 需同时命中）
- `mailto` 建议改成自己真实邮箱（OpenAlex polite pool，限流更宽松）

## 文件结构

```
main.py                      主流程（单文件，无框架依赖）
config.yaml                  画像 / 数据源 / 词表 / 阈值
state.json                   已推送论文 ID（自动维护，勿手改）
daily/YYYY-MM-DD.md          每日日报归档
.github/workflows/daily.yml  GitHub Actions 定时任务
```

## 已知边界

- OpenAlex 对部分 T&F 期刊（IJGIS 等）摘要收录不全，个别论文只有标题可判
- arXiv 窗口 2 天、OpenAlex 窗口 5 天，靠 state.json 去重，重复推送概率极低
- Server酱免费版每天 5 条消息，本系统每天只发 1 条，足够
- 周末 arXiv 不更新时可能收录 0 篇，属正常现象
