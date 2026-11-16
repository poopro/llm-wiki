#!/usr/bin/env python3
"""wiki_lint.py — LLM Wiki 健康檢查（程式關卡）

檢查項目（依 AGENTS.md）：
  1. 斷連結：[[slug]] 沒有對應的 wiki 頁面
  2. 孤兒頁：沒有任何其他頁面連進來的頁（index/log 除外）
  3. 缺出處：頁面沒有標注 raw/ 來源
  4. index 未收錄：wiki 頁沒有出現在 index.md

回傳：發現問題時 exit 1，全過 exit 0。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"

problems = []

pages = {p.stem: p for p in WIKI.glob("*.md") if p.name not in ("index.md", "log.md")}
if not pages:
    print("錯誤：wiki/ 找不到任何頁面")
    sys.exit(1)

link_re = re.compile(r"\[\[([a-z0-9\-]+)\]\]")
src_re = re.compile(r"raw/\d{2}-[A-Za-z0-9\-]+\.md")
code_re = re.compile(r"`[^`]*`")

inbound = {slug: 0 for slug in pages}
all_bodies = {}

for slug, path in pages.items():
    text = path.read_text(encoding="utf-8")
    all_bodies[slug] = text
    # 掃連結前先移除行內程式碼：`[[wikilink]]` 這類是在「提到」語法，不是真的連結
    text_no_code = code_re.sub("", text)

    # 1. 斷連結
    for target in link_re.findall(text_no_code):
        if target not in pages:
            problems.append(f"[斷連結] {path.name} -> [[{target}]] 不存在")
        else:
            inbound[target] += 1

    # 3. 缺出處
    if not src_re.search(text):
        problems.append(f"[缺出處] {path.name} 沒有標注任何 raw/ 來源")

    # 3b. 出處指向的 raw 檔案必須存在（findall 會回傳含 raw/ 前綴的整個 match，先剝掉）
    for m in src_re.findall(text):
        filename = m.split("/")[-1]
        if not (RAW / filename).exists():
            problems.append(f"[壞引用] {path.name} 引用的 {m} 在 raw/ 不存在")

# 2. 孤兒頁
for slug, count in inbound.items():
    if count == 0:
        problems.append(f"[孤兒頁] {slug}.md 沒有任何頁面連結到它")

# 4. index 未收錄
index_text = (WIKI / "index.md").read_text(encoding="utf-8")
for slug in pages:
    if f"[[{slug}]]" not in index_text:
        problems.append(f"[index 未收錄] {slug}.md 沒有出現在 index.md")

# raw/ 每個來源都應該有對應的 source 頁（ingest 完整性）
for raw_file in RAW.glob("*.md"):
    if not any(f"raw/{raw_file.name}" in t for t in all_bodies.values()):
        problems.append(f"[未 ingest] raw/{raw_file.name} 沒有任何頁面引用它")

print(f"wiki 頁面數：{len(pages)}；raw 來源數：{len(list(RAW.glob('*.md')))}")
if problems:
    print(f"發現 {len(problems)} 個問題：")
    for p in problems:
        print("  -", p)
    sys.exit(1)
print("lint 全過：無斷連結、無孤兒頁、每頁有出處、index 收錄完整。")
