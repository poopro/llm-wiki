---
type: entity
tags: [實作, 發布]
sources: [raw/04-liangdabiao-llm-wiki.md]
updated: 2026-11-16
---

# 實體：liangdabiao/llm-wiki（多來源 ingest ＋ 網站發布）

GitHub 專案 `liangdabiao/llm-wiki`：依 Karpathy 方法論，用 AI 持續建構與維護個人知識庫 [[entity-karpathy]]。

兩個特點：

1. **來源多元**：支援網頁、推特、公眾號、小紅書、知乎、YouTube、PDF、本地檔案，自動整理成結構化 wiki 頁面
2. **發布成網站**：透過 Quartz 把 wiki 發布成靜態知識庫網站——wiki 不只給 Agent 用，也直接變成可瀏覽的成果

另外它用 `claude_agent_sdk` 呼叫 claude agent 來使用 llm-wiki，並提供 API 對外提供服務。這個案例對本作業特別有參考價值：**wiki + 靜態網站發布**正是「知識庫 → 可瀏覽成品」的路線，本作業的教學 HTML 簡報走的是同一個方向（用 wiki 當唯一知識來源產出成品）。來源摘要頁：[[source-04-liangdabiao]]

出處：raw/04-liangdabiao-llm-wiki.md
