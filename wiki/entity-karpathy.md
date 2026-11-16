---
type: entity
tags: [原典, karpathy]
sources: [raw/01-karpathy-llm-wiki-gist.md]
updated: 2026-11-16
---

# 實體：Karpathy 的 LLM Wiki gist（原典）

- **作者**：Andrej Karpathy（OpenAI 創始成員、前 Tesla AI 總監）
- **形式**：GitHub gist〈LLM Wiki — A pattern for building personal knowledge bases using LLMs〉
- **性質**：一份「構想檔（idea file）」，設計成直接貼給自己的 LLM Agent（Claude Code、Codex、OpenCode 等），由 Agent 與使用者一起做出適合自己的版本

內容要點：核心觀念 [[concept-compilation]]、三層架構 [[concept-three-layers]]、三個操作 [[concept-operations]]、導航檔案 [[concept-index-log]]。附錄的技巧：Obsidian graph view 看知識圖形、Marp 從 wiki 直接生投影片、Dataview 對 frontmatter 做查詢。

文中把這個模式的思想來源追溯到 Vannevar Bush 1945 年的 **Memex**：私人、主動策展、文件間的「聯想路徑」與文件本身同樣有價值。原文結尾點出 Memex 解決不了、而 LLM 能解決的問題是——**「誰來做維護」**：人類放棄維護知識庫，是因為維護成本成長得比價值快；LLM 不會無聊、不會忘記更新交叉引用、一次可以碰 15 個檔案。

相關頁面：[[overview]]、[[synthesis-failures]]；來源摘要頁：[[source-01-karpathy]]

出處：raw/01-karpathy-llm-wiki-gist.md
