---
type: concept
tags: [core]
sources: [raw/01-karpathy-llm-wiki-gist.md]
updated: 2026-11-16
---

# 核心觀念：知識編譯（Compile Once, Keep Current）

Karpathy 把一般人和 LLM 相處的方式稱為 RAG 模式：上傳一堆檔案，查詢時 LLM 撈出相關片段、重新拼出答案。他點出的問題是——**LLM 每次都在「從頭重新發現知識」，沒有任何累積** [[entity-karpathy]]。

LLM Wiki 的差別：新資料進來時，LLM 不是先建索引等查詢，而是**立刻讀完、萃取重點、編入現有 wiki**——更新實體頁、修訂主題摘要、標注新資料與舊主張的矛盾。原文的說法是「知識被編譯一次然後保持更新，而不是每次查詢重新推導」。

這讓 wiki 成為一個**持續複利（compounding）的資產**：交叉引用已經建好、矛盾已經標注、綜合已經反映讀過的一切 [[overview]]。

分工原則：人負責選來源、探索、問好問題；LLM 負責所有苦工——摘要、交叉引用、歸檔、記帳。Karpathy 的比喻：Obsidian 是 IDE，LLM 是程式設計師，wiki 是程式碼庫。

出處：raw/01-karpathy-llm-wiki-gist.md
