# Index — LLM Wiki（主題：LLM Wiki 模式本身）

> 查詢時先讀本頁找相關頁面，再深入內容。每次 ingest 更新。

## 綜述

- [[overview]] — LLM Wiki 是什麼：一句話核心主張 + 全 wiki 導覽

## 概念（concept）

- [[concept-compilation]] — 核心觀念：知識編譯一次、持續維護，而非每次查詢重新推導
- [[concept-three-layers]] — 三層架構：raw（不可改）/ wiki（LLM 維護）/ schema（手冊）
- [[concept-operations]] — 三個操作：Ingest、Query、Lint 的標準流程
- [[concept-index-log]] — index.md 與 log.md：百頁規模內不需要向量資料庫

## 比較（comparison）

- [[comparison-vs-rag]] — LLM Wiki vs RAG：整理時機、累積性、矛盾處理、成本曲線

## 實體（entity）

- [[entity-karpathy]] — 原典：Karpathy 的 gist，與 Memex（1945）的思想連結
- [[entity-student-llm-wiki]] — 學生課程知識庫：簡報進、wiki 出
- [[entity-mindbase]] — MindBase：lint 從 AI 判斷改成程式計算
- [[entity-liangdabiao]] — 多來源 ingest ＋ Quartz 靜態網站發布
- [[entity-crow]] — CROW：ingest 決策佔 72% token 的量化研究

## 綜合分析（synthesis）

- [[synthesis-failures]] — 七種常見失敗模式與社群對策（近重複、斷連結、靜默覆蓋…）

## 來源摘要（source）

- [[source-01-karpathy]] — Karpathy gist 原文（2026-04-04）
- [[source-02-student]] — student-llm-wiki（課程情境）
- [[source-03-mindbase]] — mindbase-llm-wiki（lint 程式化）
- [[source-04-liangdabiao]] — liangdabiao/llm-wiki（多來源、Quartz）
- [[source-05-crow]] — crow llm-wiki-v2（決策成本研究）
- [[source-06-awesome]] — awesome-llm-wiki（生態清單）
