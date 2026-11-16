---
type: concept
tags: [core, navigation]
sources: [raw/01-karpathy-llm-wiki-gist.md, raw/03-mindbase-llm-wiki.md]
updated: 2026-11-16
---

# 兩個特殊檔案：index.md 與 log.md

Karpathy 用兩個檔案讓 wiki 隨著規模成長還能被導航 [[entity-karpathy]]：

## index.md（內容導向）

整個 wiki 的目錄：每頁一條連結＋一句話摘要，可加日期、來源數等 metadata，依分類（實體、概念、來源…）組織。每次 ingest 都要更新。**查詢時 Agent 先讀 index 找相關頁，再鑽進頁面**——在約百份來源、數百頁的規模下效果出奇地好，不需要 embedding 向量資料庫。

## log.md（時間導向）

append-only 的操作紀錄：ingest、query、lint 都記一筆。實用技巧是讓每條開頭格式固定（例如 `## [2026-04-02] ingest | 文章標題`），就能用 unix 工具解析：`grep "^## \[" log.md | tail -5` 看最近五筆。log 提供知識庫的演化時間線，也讓 Agent 知道最近做過什麼。

MindBase 把這個觀念再往前推一步：每次查詢都追加到 `logs/<date>.md`，記錄「讀了哪幾頁 vs 實際引用了哪幾頁」——如果「wiki 裡明明有、模型卻沒用到」，事後可以用 grep 找出來 [[entity-mindbase]]。

出處：raw/01-karpathy-llm-wiki-gist.md、raw/03-mindbase-llm-wiki.md
