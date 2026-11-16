---
type: concept
tags: [core, architecture]
sources: [raw/01-karpathy-llm-wiki-gist.md]
updated: 2026-11-16
---

# 三層架構：raw / wiki / schema

LLM Wiki 把知識庫分成三層，每一層的「誰可以寫」都不同 [[entity-karpathy]]：

| 層 | 內容 | 誰擁有 |
|---|---|---|
| **raw/**（原始來源） | 文章、論文、逐字稿、資料檔 | **不可修改**，是 source of truth，Agent 只讀不寫 |
| **wiki/**（知識頁） | 摘要、實體頁、概念頁、比較、綜述 | LLM 全權生成與維護：建頁、更新、維護交叉引用、保持一致 |
| **schema**（手冊） | `AGENTS.md` / `CLAUDE.md`：結構、慣例、ingest/query/lint 的工作流程 | 人與 Agent 共同演化 |

schema 是「讓 LLM 成為有紀律的 wiki 維護者，而不是一般聊天機器人」的關鍵：它把讀者、頁面類型、出處格式、矛盾處理原則事先講清楚。本 wiki 的 schema 就是 [[../../AGENTS.md | AGENTS.md]]（倉庫根目錄），由「先討論、後生成」的需求訪談產生（見 notes/requirements-discussion.md）。

整個 wiki 就是一個 git repo，版本歷史、分支、協作都是現成的 [[entity-karpathy]]。

出處：raw/01-karpathy-llm-wiki-gist.md
