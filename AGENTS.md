# AGENTS.md — LLM Wiki 維護手冊

這個資料夾是一個依 Karpathy「LLM Wiki」模式運作的个人知識庫（schema）。
任何 LLM Agent 在此資料夾工作時，必須遵守本手冊。

- **主題**：LLM Wiki 模式本身（核心觀念、操作、與 RAG 的差異、實作案例）
- **讀者**：不熟悉此主題的同學與助教 → 頁面要能獨立閱讀，名詞第一次出現要有解釋
- **語言**：台灣習慣的繁體中文；專案名稱與技術名詞保留英文原文

## 資料夾結構（三層架構）

```
llm-wiki/
├── AGENTS.md        ← 本手冊（schema）：Agent 唯一允許修改的規則檔
├── raw/             ← 原始來源，不可修改（Agent 只讀不寫）
├── wiki/            ← Agent 生成與維護的頁面（Agent 全權負責）
│   ├── index.md     ← 目錄：所有頁面 + 一句話摘要
│   └── log.md       ← 日誌：append-only，記錄每次 ingest / query / lint
├── scripts/         ← 檢查腳本（wiki_lint.py）
└── topic-llm-wiki-slides/  ← 下游產出：教學 HTML 簡報的工作目錄
```

## 頁面規範

- 檔名即 slug（英文小寫連字號），頁內標題用中文。
- 每頁開頭加 YAML frontmatter：

```yaml
---
type: overview | concept | entity | comparison | source | synthesis
tags: [...]
sources: [raw/XX-....md]
updated: YYYY-MM-DD
---
```

- 引用其他頁面一律用 `[[slug]]`。
- **每頁必須有出處**：正文最後一行寫 `出處：raw/XX-....md`（多個來源並列）。
- 關鍵數字（百分比、天數、計數）逐句標來源，不得憑記憶填。
- 資料互相矛盾時：並列保留、標注各自來源與差異原因，不擅自刪改或硬統一。

## 操作流程（Operations）

### Ingest（一次一篇）

1. 讀 `raw/` 新來源，寫一篇 `wiki/source-XX-短名.md` 摘要頁。
2. 更新 2–5 篇相關的 concept / entity / comparison / synthesis 頁（能連就連，擴充而不重複建頁）。
3. 更新 `wiki/index.md`（新頁 + 一句話摘要）。
4. 在 `wiki/log.md` 附加一條 `## [日期] ingest | 來源名`，列出具體改了哪些頁。
5. 跑 `python scripts/wiki_lint.py`，有錯當輪修完。
6. `git commit -m "ingest XX: 來源名"`。

### Query

- 先讀 `wiki/index.md` 找相關頁，再深入頁面，回答時標注依據的頁面。
- 有價值的比較或分析，回寫成新頁面（例如 comparison 頁），不要讓結果留在對話裡。

### Lint（健康檢查）

- **程式檢查**：`python scripts/wiki_lint.py` → 斷連結、孤兒頁、缺出處、index 未收錄。
- **人工/AI 審查**：近重複頁（同一概念兩頁）、過時主張、矛盾未標注。
- 發現問題當輪修復，並在 `log.md` 記錄。

## 停止條件

- 資料不足以支撐某個主張時，寫「來源未涵蓋」，不得用常識硬湊。
- 修改最多 3 輪仍未通過檢查就停下報告，不要無限迴圈。

## 下游產出：教學 HTML 簡報

工作目錄 `topic-llm-wiki-slides/`，流程與檢查關卡見 `topic-llm-wiki-slides/outline.md` 與 `scripts/deck_check.py`：
只能引用 wiki 頁面、每頁標出處、8–15 頁、渲染後不得溢出。
