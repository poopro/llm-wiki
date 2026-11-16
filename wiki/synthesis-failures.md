---
type: synthesis
tags: [失敗模式, 社群經驗]
sources: [raw/01-karpathy-llm-wiki-gist.md, raw/03-mindbase-llm-wiki.md, raw/05-crow-llm-wiki-v2.md]
updated: 2026-11-16
---

# 綜合分析：常見失敗模式與社群對策

綜合 gist 原文與三個實作專案的經驗，LLM Wiki 最常見的失敗模式如下 [[entity-karpathy]] [[entity-mindbase]] [[entity-crow]]：

| # | 失敗模式 | 對策 | 來源 |
|---|---|---|---|
| 1 | **近重複頁**：同一概念被建成兩頁，知識分裂 | 「Extend, don't create」——建新頁前先查 index、搜尋既有頁；MindBase 在 lint 時程式化偵測近重複 | gist 留言（podcast-wiki）、raw/03 |
| 2 | **斷連結 / 斷引用**：`[[link]]` 沒有對應頁、引用的檔案被移走 | 在 lint 時用**程式碼**計算，不靠模型判斷，避免誤報 | raw/03 |
| 3 | **靜默覆蓋**：新來源與舊主張矛盾時直接改掉 | 矛盾不刪除，集中放在「Disagreements & open questions」區塊並標注雙方來源——podcast-wiki 說這反而是最有趣的章節 | raw/01 留言 |
| 4 | **摘要越接越長**：把新內容 append 到舊摘要後面 | 「Rewrite the summary, don't append」——重新改寫，不要堆疊 | raw/01 留言 |
| 5 | **頁面漂移合流**：多頁漸漸變成同一個主題 | 定期跑一次「dream pass」合併漂移的頁面 | raw/01 留言 |
| 6 | **ingest 成本高**：token 大量花在分類、合併等「決策」 | 把決策交給小型 typed classifier，LLM 只負責寫文字；crow 實測答對率 62%→89%、ingest 時間減半 | raw/05 |
| 7 | **模型沒用該用的頁**：wiki 有資料但回答沒引用 | MindBase 記錄「讀了幾頁 vs 引用幾頁」，讓這種失敗可以被 grep 事後追蹤 | raw/03 |

這些對策的共同點：**能程式化檢查的就寫成腳本**（1、2、7），剩下需要語意的才交給 LLM 或人（3、4、5）。本 wiki 的 `scripts/wiki_lint.py` 即依此原則實作斷連結、孤兒頁、缺出處三項程式檢查。

出處：raw/01-karpathy-llm-wiki-gist.md、raw/03-mindbase-llm-wiki.md、raw/05-crow-llm-wiki-v2.md
