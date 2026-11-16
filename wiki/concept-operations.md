---
type: concept
tags: [core, operations]
sources: [raw/01-karpathy-llm-wiki-gist.md, raw/03-mindbase-llm-wiki.md]
updated: 2026-11-16
---

# 三個操作：Ingest、Query、Lint

Karpathy 的 LLM Wiki 只有三個日常操作 [[entity-karpathy]]：

## Ingest（編入）

丟一份新來源進 `raw/`，Agent 的標準流程：讀來源 →（和人討論重點）→ 寫摘要頁 → 更新 index → 更新相關的實體頁與概念頁 → 記 log。**一份來源可能碰 10–15 個 wiki 頁**。Karpathy 偏好一次 ingest 一篇、過程中參與檢查；也可以批次低監督處理，工作流由自己定義並寫進 schema。

## Query（查詢）

Agent 先讀 `index.md` 找相關頁，再深入頁面內容，答案要帶出處。答案的形式可以是比較表、頁面、投影片（Marp）、圖表。重點洞見：**好的答案應該回寫進 wiki 成為新頁面**，讓探索的成果像 ingest 的來源一樣累積，不要消失在聊天紀錄裡。

## Lint（健康檢查）

定期請 Agent 體檢 wiki：頁面間的矛盾、被新來源超越的過時主張、沒有任何入連結的孤兒頁、被提到卻沒有獨立頁面的重要概念、缺漏的交叉引用、可以靠補資料解決的空缺 [[entity-karpathy]]。

社群實作把 lint 更往前推：MindBase 在**程式碼層級**計算斷連結（`[[wikilink]]` 沒有對應頁）與斷引用（`[@path]` 指向被移動或刪除的檔案），不經過模型判斷，所以沒有誤報 [[entity-mindbase]]。

出處：raw/01-karpathy-llm-wiki-gist.md、raw/03-mindbase-llm-wiki.md
