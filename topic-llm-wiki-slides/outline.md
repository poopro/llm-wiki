# outline.md — 簡報大綱與流程關卡定義

## 這個 workflow 的 loop 五要素（依上課框架）

| 要素 | 內容 |
|---|---|
| 🎯 目標 | 只用 wiki 頁面，產出讓不熟悉主題的人能懂的教學 HTML 簡報 |
| 🚧 限制 | 不得使用 wiki 以外的知識；每頁標出處；8–15 頁；渲染後不得溢出；渲染時不得改字 |
| ✅ 完成標準 | `deck_check.py` 全過（頁數、每頁出處、引用頁存在、覆蓋率≥3 頁）＋瀏覽器逐頁無溢出＋忠實度審查通過 |
| 🛑 停止條件 | 全過 / 修滿 3 輪 / wiki 相關頁面少於 3 頁一開始就停 |
| ⏰ 觸發 | 使用者說「用 wiki 做 LLM Wiki 主題的教學簡報」 |

## Graph（哪一關只能看什麼、不能做什麼）

```
檢索 wiki (sources.md)
  └─ 覆蓋率關卡：相關頁 < 3 → 停止
       └─ 證據卡 ×6（平行；只能看一篇 raw 來源，不得混入其他來源）
            └─ 大綱（outline.md）
                 └─ 忠實度檢查：大綱與卡片矛盾 → 退回修大綱或補檢索
                      └─ 逐頁稿（drafts/slides-v1.md）
                           └─ 程式檢查（deck_check.py）→ 退回只修有問題那頁
                                └─ 渲染（deck.html）→ 瀏覽器溢出檢查 → 退回渲染（不得改字）
                                     └─ AI 審查（新對話：只給成品＋引用頁）→ 退回逐頁稿
                                          └─ 交件（report.md 附檢查紀錄）
```

## 12 頁大綱（每頁標出處）

| # | 標題 | 重點 | 依據 wiki 頁 |
|---|---|---|---|
| 1 | LLM Wiki：會自己長大的知識庫 | 開場、一句話定義 | overview |
| 2 | 痛點：AI 每次都從頭找 | RAG 沒有累積；ChatGPT 上傳/NotebookLM 屬於這類 | concept-compilation、comparison-vs-rag |
| 3 | 核心觀念：編譯一次 | ingest 時就整理，交叉引用、矛盾標注都是維護時完成的 | concept-compilation |
| 4 | 三層架構 | raw（不可改）/ wiki（LLM 維護）/ schema（AGENTS.md） | concept-three-layers |
| 5 | 三個操作 | Ingest / Query / Lint 總覽 | concept-operations |
| 6 | Ingest：一篇資料進來會怎樣 | 讀→討論→摘要頁→更新相關頁→log；一份來源碰 10–15 頁 | concept-operations、source-01-karpathy |
| 7 | Query：回答要帶出處 | 先讀 index、好答案回寫 wiki、讀了 vs 引用要可追蹤 | concept-operations、concept-index-log、entity-mindbase |
| 8 | Lint：幫 wiki 健康檢查 | 程式檢查（斷連結/孤兒頁）＋語意檢查（矛盾/過時） | concept-operations、entity-mindbase、synthesis-failures |
| 9 | index.md 與 log.md | 百頁規模內 index 就夠、不需要向量資料庫；log 可 grep | concept-index-log |
| 10 | LLM Wiki vs RAG | 六個面向比較表 | comparison-vs-rag |
| 11 | 真實案例與數據 | 學生課程 wiki、MindBase、crow 的 72%/62%→89% | entity-student-llm-wiki、entity-mindbase、entity-crow、entity-liangdabiao |
| 12 | 總結 | 七種失敗模式對策、一句話帶走、生態成型 | synthesis-failures、overview、source-06-awesome |

人工確認關卡：大綱由使用者核可後才進逐頁稿。
