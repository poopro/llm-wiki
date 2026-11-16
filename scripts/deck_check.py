#!/usr/bin/env python3
"""deck_check.py — 教學 HTML 簡報的程式檢查關卡

檢查項目（依 outline.md 的完成標準）：
  1. 頁數 8–15
  2. 每頁有「來源：」標注
  3. 每頁引用的 wiki 頁面真的存在
  4. 覆蓋率：被引用的相異 wiki 頁 ≥ 3（老師的停止條件）

回傳：發現問題時 exit 1，全過 exit 0。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DECK = ROOT / "topic-llm-wiki-slides" / "deck.html"
WIKI = ROOT / "wiki"

problems = []
html = DECK.read_text(encoding="utf-8")

sections = re.findall(r'<section class="slide[^"]*"[^>]*data-src="([^"]+)"(.*?)</section>',
                      html, flags=re.S)
n = len(sections)
if not 8 <= n <= 15:
    problems.append(f"[頁數] 簡報有 {n} 頁，需 8–15 頁")

cited_pages = set()
for idx, (srcs, body) in enumerate(sections, start=1):
    for src in [s.strip() for s in srcs.split(",")]:
        cited_pages.add(src)
        if not (WIKI.parent / src).exists():
            problems.append(f"[引用不存在] 第 {idx} 頁引用的 {src} 不在 wiki/")

    if "來源：" not in body:
        problems.append(f"[缺出處] 第 {idx} 頁沒有「來源：」標注")

if len(cited_pages) < 3:
    problems.append(f"[覆蓋率] 只引用 {len(cited_pages)} 頁 wiki，需 ≥ 3 頁")

print(f"簡報頁數：{n}；引用的 wiki 頁面：{len(cited_pages)} 頁")
if problems:
    print(f"發現 {len(problems)} 個問題：")
    for p in problems:
        print("  -", p)
    sys.exit(1)
print("deck_check 全過：頁數、每頁出處、引用頁存在、覆蓋率都合格。")
