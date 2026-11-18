#!/usr/bin/env python3
"""build_site.py — 把 wiki/ 的 Markdown 頁面渲染成 GitHub Pages 靜態網站

規則（依 AGENTS.md「網站生成」）：
  - wiki/ 每一頁都會變成 site/<slug>.html，[[slug]] 自動轉成站內連結
  - 根目錄 index.html 由本腳本生成（總覽 + 分類目錄 + 簡報連結），不要手改
  - 改完 wiki 後跑：python scripts/build_site.py → commit → Pages 自動上線

頁面分類順序：overview → concept → comparison → entity → synthesis → source → log
"""
import re
import subprocess
import sys
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
SITE = ROOT / "site"
REPO_URL = "https://github.com/poopro/llm-wiki"
DECK_URL = "topic-llm-wiki-slides/deck.html"

TYPE_LABEL = {
    "overview": "綜述",
    "concept": "概念",
    "comparison": "比較",
    "entity": "實體",
    "synthesis": "綜合分析",
    "source": "來源摘要",
}
TYPE_ORDER = ["overview", "concept", "comparison", "entity", "synthesis", "source"]

BASE_CSS = """
  :root { --bg:#0f172a; --card:#1e293b; --ink:#e2e8f0; --dim:#94a3b8; --accent:#fbbf24; --link:#818cf8; }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--bg); color:var(--ink); font-family:"Microsoft JhengHei",system-ui,-apple-system,sans-serif; line-height:1.8; }
  .wrap { max-width:880px; margin:0 auto; padding:24px 20px 60px; }
  nav { display:flex; gap:18px; align-items:center; padding:14px 0; border-bottom:1px solid var(--card); margin-bottom:28px; flex-wrap:wrap; }
  nav a { color:var(--dim); text-decoration:none; font-size:15px; }
  nav a:hover { color:var(--accent); }
  nav .brand { color:var(--accent); font-weight:bold; font-size:17px; margin-right:auto; }
  h1 { color:var(--accent); font-size:30px; margin-bottom:18px; }
  h2 { color:var(--accent); font-size:22px; margin:26px 0 10px; }
  p { margin-bottom:14px; }
  ul { margin:0 0 14px 22px; }
  li { margin-bottom:6px; }
  a { color:var(--link); }
  table { border-collapse:collapse; width:100%; margin-bottom:16px; font-size:15px; }
  th,td { border:1px solid #334155; padding:8px 12px; text-align:left; }
  th { background:var(--card); color:var(--accent); }
  code { background:var(--card); padding:2px 6px; border-radius:5px; font-size:14px; }
  pre code { display:block; padding:14px; overflow-x:auto; }
  .meta { color:var(--dim); font-size:14px; margin-bottom:22px; }
  .card { background:var(--card); border-radius:12px; padding:16px 20px; margin-bottom:12px; }
  .card b a { color:var(--ink); text-decoration:none; font-size:16px; }
  .card b a:hover { color:var(--accent); }
  .card small { color:var(--dim); display:block; margin-top:4px; }
  .hero { text-align:center; padding:30px 0 10px; }
  .hero h1 { font-size:34px; }
  .hero .sub { color:var(--dim); margin-bottom:26px; }
  .btn { display:inline-block; background:var(--accent); color:#0f172a; font-weight:bold; text-decoration:none;
         padding:10px 22px; border-radius:10px; margin:0 6px 10px; }
  .btn.ghost { background:var(--card); color:var(--ink); }
  footer { margin-top:40px; color:var(--dim); font-size:13px; border-top:1px solid var(--card); padding-top:16px; }
"""


def parse_page(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    fm = {}
    if text.startswith("---\n"):
        end = text.index("\n---", 4)
        fm = yaml.safe_load(text[4:end]) or {}
        text = text[end + 4:]
    m = re.search(r"^# (.+)$", text, flags=re.M)
    title = m.group(1).strip() if m else path.stem
    return {"slug": path.stem, "fm": fm, "title": title, "md": text.strip()}


def wikilinks_to_md(md_text: str) -> str:
    """[[slug]] → [label](site/slug.html)；repo 內路徑 → GitHub 連結。"""

    def repl(m):
        inner = m.group(1)
        if "|" in inner:
            target, label = [s.strip() for s in inner.split("|", 1)]
        else:
            target, label = inner.strip(), inner.strip()
        if "/" in target:  # 例如 ../../AGENTS.md → repo 連結
            name = target.rsplit("/", 1)[-1]
            return f"[{label}]({REPO_URL}/blob/main/{name})"
        return f"[{label}](site/{target}.html)"

    return re.sub(r"\[\[([^\]]+)\]\]", repl, md_text)


def page_html(page: dict, body_html: str) -> str:
    t = page["fm"].get("type", "")
    label = TYPE_LABEL.get(t, "操作日誌")
    updated = page["fm"].get("updated", "")
    sources = page["fm"].get("sources") or []
    src_links = "、".join(
        f'<a href="{REPO_URL}/blob/main/{s}">{s}</a>' for s in sources
    )
    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page['title']} — LLM Wiki</title>
<style>{BASE_CSS}</style>
</head>
<body>
<div class="wrap">
<nav><span class="brand">LLM Wiki</span><a href="index.html">目錄</a><a href="log.html">日誌</a><a href="../{DECK_URL}">教學簡報</a><a href="{REPO_URL}">GitHub</a></nav>
<div class="meta">{label} · 更新 {updated} · 來源：{src_links}</div>
{body_html}
<footer>本頁由 <code>wiki/{page['slug']}.md</code> 自動生成（scripts/build_site.py）· 內容依 AGENTS.md 規則維護</footer>
</div>
</body>
</html>
"""


def main() -> None:
    SITE.mkdir(exist_ok=True)
    pages = [parse_page(p) for p in WIKI.glob("*.md")]
    by_slug = {p["slug"]: p for p in pages}

    # 每一頁 → site/<slug>.html
    for page in pages:
        html_body = markdown.markdown(
            wikilinks_to_md(page["md"]), extensions=["tables", "fenced_code"]
        )
        (SITE / f"{page['slug']}.html").write_text(page_html(page, html_body), encoding="utf-8")

    # 根目錄 index.html：總覽 + 分類目錄
    cards = []
    for t in TYPE_ORDER:
        group = [p for p in pages if p["fm"].get("type") == t]
        if not group:
            continue
        cards.append(f"<h2>{TYPE_LABEL[t]}</h2>")
        for p in group:
            summary = next(
                (l for l in by_slug["index"]["md"].splitlines() if f"[[{p['slug']}]]" in l and "—" in l),
                "",
            )
            desc = summary.split("—", 1)[1].strip() if summary else ""
            cards.append(
                f'<div class="card"><b><a href="site/{p["slug"]}.html">{p["title"]}</a></b>'
                f"<small>{desc}</small></div>"
            )
    log = next((p for p in pages if p["slug"] == "log"), None)
    if log:
        cards.append(f'<h2>過程紀錄</h2><div class="card"><b><a href="site/log.html">{log["title"]}</a></b>'
                     "<small>ingest / lint / query / slides 的完整操作日誌</small></div>")

    index_html = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LLM Wiki — 主題知識庫</title>
<style>{BASE_CSS}</style>
</head>
<body>
<div class="wrap">
<div class="hero">
<h1>LLM Wiki</h1>
<div class="sub">用 Karpathy 的 LLM Wiki 模式建立的主題知識庫——主題就是「LLM Wiki 模式本身」<br>18 個知識頁 · 6 篇 raw 來源 · 每頁標注出處 · AGENTS.md 規則驅動</div>
<a class="btn" href="../{DECK_URL}">看教學簡報</a>
<a class="btn ghost" href="site/overview.html">從綜述開始讀</a>
<a class="btn ghost" href="{REPO_URL}">GitHub Repo</a>
</div>
{''.join(cards)}
<footer>頁面由 <code>scripts/build_site.py</code> 從 <code>wiki/*.md</code> 自動生成 · 維護規則見 <a href="{REPO_URL}/blob/main/AGENTS.md">AGENTS.md</a> · NYCU 114481030 陳宏威</footer>
</div>
</body>
</html>
"""
    (ROOT / "index.html").write_text(index_html, encoding="utf-8")

    # 舊的 hash 會殘留，確保 site/ 沒有多餘檔案
    try:
        head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True).stdout.strip()
    except Exception:
        head = "?"
    print(f"生成完成：site/ 共 {len(pages)} 頁 + 根目錄 index.html（git {head}）")


if __name__ == "__main__":
    main()
