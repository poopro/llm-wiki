---
type: overview
tags: [core, 綜述]
sources: [raw/01-karpathy-llm-wiki-gist.md]
updated: 2026-11-16
---

# LLM Wiki 是什麼？（綜述）

LLM Wiki 是 Andrej Karpathy 在 2026 年 4 月提出的一種「用 LLM 建立並維護個人知識庫」的模式 [[entity-karpathy]]。

它的核心主張只有一句：**知識要「編譯」一次、持續維護，而不是每次查詢都重新推導** [[concept-compilation]]。

做法是把知識庫分成三層：不可修改的原始來源 `raw/`、由 LLM 全權維護的 `wiki/` 頁面、以及規範 Agent 行為的 schema（`AGENTS.md`）[[concept-three-layers]]。日常只有三個操作：**Ingest**（把新資料編入 wiki）、**Query**（查詢並回寫好答案）、**Lint**（健康檢查）[[concept-operations]]，再靠 `index.md` 與 `log.md` 兩個特殊檔案導航 [[concept-index-log]]。

和傳統 RAG 的差別，在於 RAG 每次回答都是「從原始文件重新拼湊」，而 LLM Wiki 的交叉引用、矛盾標注、綜合摘要都已經在維護時完成了 [[comparison-vs-rag]]。這個模式已經有許多真實實作，例如學生課程知識庫 [[entity-student-llm-wiki]]、把 lint 程式化的 MindBase [[entity-mindbase]]、多來源 ingest 的 liangdabiao 版 [[entity-liangdabiao]]，以及研究 ingest 決策成本的 crow [[entity-crow]]。

實作上的常見失敗模式與社群對策，整理在 [[synthesis-failures]]。更多實作專案的完整清單收錄在 Awesome LLM Wiki [[source-06-awesome]]。

出處：raw/01-karpathy-llm-wiki-gist.md
