---
type: comparison
tags: [rag, 比較]
sources: [raw/01-karpathy-llm-wiki-gist.md, raw/05-crow-llm-wiki-v2.md]
updated: 2026-11-16
---

# 比較：LLM Wiki vs RAG

| 面向 | 傳統 RAG | LLM Wiki |
|---|---|---|
| 知識何時被整理 | 查詢時現場撈片段、現場拼答案 | ingest 時就讀完、萃取、編入頁面 |
| 累積性 | 沒有累積，每次從頭推導 | wiki 是持久、複利的資產 [[concept-compilation]] |
| 交叉引用 | 沒有；靠 embedding 相似度 | 已經建好，頁與頁互連 |
| 矛盾處理 | 兩個片段都撈得到，誰對沒人說 | 維護時已標注「矛盾與開放問題」[[synthesis-failures]] |
| 基礎建設 | 需要 embedding、向量索引 | 中小規模只要 index.md 就夠 [[concept-index-log]] |
| 成本曲線 | 每次查詢都要重新檢索＋拼湊 | 維護成本一次性；crow 的研究指出 ingest 的 token 有 72% 花在「決策」而非撰寫，把決策交給小型分類器後 ingest 時間可減半 [[entity-crow]] |

Karpathy 原文對 NotebookLM、ChatGPT 檔案上傳等系統的定位：它們都屬於 RAG 式——「works, but the LLM is rediscovering knowledge from scratch on every question」[[entity-karpathy]]。

注意：兩者不是敵對關係。Karpathy 也提到，規模更大時可以在 wiki 上加搜尋引擎（如 qmd：BM25/向量混合檢索）；wiki 模式改變的是「知識有沒有被整理過」，不是禁止檢索技術。

出處：raw/01-karpathy-llm-wiki-gist.md、raw/05-crow-llm-wiki-v2.md
