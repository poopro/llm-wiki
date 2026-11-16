# LLM Wiki — 個人知識庫實作（TAICA 生成式AI 第十週作業）

主題：**Karpathy 的 LLM Wiki 模式本身**。用 LLM Wiki 來整理 LLM Wiki——raw 來源是 Karpathy 的 gist 原文與五個真實實作專案。

## 成品連結

- 教學 HTML 簡報：<https://poopro.github.io/llm-wiki/>（自動跳轉到簡報）
- 直接開簡報：<https://poopro.github.io/llm-wiki/topic-llm-wiki-slides/deck.html>

## 這個 repo 是什麼

```
llm-wiki/
├── AGENTS.md              ← Wiki 的維護手冊（schema），LLM Agent 依此運作
├── notes/                 ← 「先討論、後生成」的需求訪談與摘要紀錄
├── raw/                   ← 6 篇原始來源（不可修改）：gist 原文 + 5 個實作專案
├── wiki/                  ← LLM 生成維護的知識頁（overview/concept/entity/comparison/source/synthesis）
│   ├── index.md           ← 目錄
│   └── log.md             ← 操作日誌（ingest/lint/query 全紀錄）
├── scripts/
│   ├── wiki_lint.py       ← lint 關卡：斷連結、孤兒頁、缺出處、index 未收錄
│   └── deck_check.py      ← 簡報關卡：頁數、每頁出處、引用頁存在
└── topic-llm-wiki-slides/ ← 簡報工作目錄：sources / cards / outline / drafts / deck.html / report.md
```

## 怎麼跑檢查

```bash
python scripts/wiki_lint.py    # wiki 健康檢查
python scripts/deck_check.py   # 簡報內容檢查
```

## 來源

- Karpathy, *LLM Wiki*（gist, 2026-04）：<https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- 其餘 5 篇來源見 `wiki/index.md` 的 source 分類。

作者：NYCU 114481030 陳宏威（2026-11）
