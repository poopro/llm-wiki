# drafts/slides-v1.md — 逐頁稿（第一版）

> 節點權限：只依已通過的大綱＋對應證據卡寫，不得引用卡片以外的內容。
> 檢查關卡：deck_check.py（程式）→ 渲染溢出（瀏覽器）→ 忠實度審查（只給逐頁稿與引用頁）。

## 投影片 1（來源：wiki/overview.md）
LLM Wiki — 會自己長大的知識庫
一句話：讓 AI 把你讀過的資料「編譯」成互相連結的 wiki，並持續維護。
教學簡報 · 內容全部來自本 repo 的 LLM Wiki · NYCU 114481030 陳宏威

## 投影片 2（來源：wiki/concept-compilation.md、wiki/comparison-vs-rag.md）
痛點：AI 每次都從頭找
- 上傳一堆檔案，查詢時才撈相關片段、現場拼答案
- LLM 每次都「從頭重新發現知識」，沒有累積
- 需要綜合五份文件的問題，每次都要重新找、重新拼
- NotebookLM、ChatGPT 檔案上傳都屬於這類（RAG）
關鍵句：沒有東西被累積。

## 投影片 3（來源：wiki/concept-compilation.md）
核心觀念：編譯一次，持續維護
- 新資料進來：立刻讀完、萃取、編入現有 wiki
- 交叉引用已建好、矛盾已標注、綜合已反映讀過的一切
- wiki 是持久、複利（compounding）的資產
分工：人選來源、問好問題；LLM 做摘要、歸檔、記帳。

## 投影片 4（來源：wiki/concept-three-layers.md）
三層架構
- raw/ 原始來源：不可修改，source of truth，Agent 只讀不寫
- wiki/ 知識頁：LLM 全權生成與維護（建頁、更新、交叉引用）
- schema（AGENTS.md）：規範結構、慣例與工作流，人與 Agent 共同演化
補充：整個 wiki 就是一個 git repo——版本歷史是現成的。

## 投影片 5（來源：wiki/concept-operations.md）
三個操作
- Ingest：把新來源讀完、編入相關頁面
- Query：先讀 index 找頁面，答案帶出處
- Lint：定期健康檢查

## 投影片 6（來源：wiki/concept-operations.md、wiki/source-01-karpathy.md）
Ingest：一篇資料進來會發生什麼
讀來源 → 與你討論重點 → 寫摘要頁 → 更新相關的實體/概念頁 → 更新 index、記 log
- 一份來源可能碰 10–15 個 wiki 頁
- Karpathy 偏好一次一篇、邊做邊檢查

## 投影片 7（來源：wiki/concept-operations.md、wiki/concept-index-log.md、wiki/entity-mindbase.md）
Query：回答要帶出處
- 先讀 index.md 找相關頁，再深入內容
- 好答案回寫進 wiki，不要消失在聊天紀錄
- MindBase：記錄「讀了哪幾頁 vs 引用了哪幾頁」——該用而沒用的頁，事後 grep 得到

## 投影片 8（來源：wiki/concept-operations.md、wiki/entity-mindbase.md、wiki/synthesis-failures.md）
Lint：幫 wiki 健康檢查
- 程式檢查：斷連結、斷引用、近重複頁（不經模型判斷 → 沒有誤報）
- 語意檢查：矛盾、過時主張、缺頁
- 社群口訣：Extend, don't create——擴充既有頁，不要再建一頁

## 投影片 9（來源：wiki/concept-index-log.md）
index.md 與 log.md
- index.md：每頁一句話摘要，每次 ingest 更新；查詢的入口
- log.md：append-only；固定前綴（## [日期] 操作 | 標題）就能用 grep 解析
- 百頁規模：光靠 index 就夠，不需要向量資料庫

## 投影片 10（來源：wiki/comparison-vs-rag.md）
LLM Wiki vs RAG
| 面向 | RAG | LLM Wiki |
|---|---|---|
| 整理時機 | 查詢時現場拼 | ingest 時就整理 |
| 累積性 | 沒有 | 持久、複利 |
| 交叉引用 | 無 | 已建好 |
| 矛盾 | 片段都撈得到 | 已標注 |
| 基礎建設 | embedding、向量索引 | index.md 就夠 |
| 成本 | 每次查詢重付 | 維護一次性 |

## 投影片 11（來源：wiki/entity-student-llm-wiki.md、wiki/entity-mindbase.md、wiki/entity-crow.md、wiki/entity-liangdabiao.md）
真實案例與數據
- Student LLM Wiki：課程簡報 → wiki，Feynman 複習、弱點追蹤
- MindBase：lint 程式化——斷連結/斷引用由程式計算，沒有誤報
- CROW：ingest 的 token 有 72% 花在「決策」；交給小型分類器後 62%→89%、時間減半
- liangdabiao：多來源 ingest，用 Quartz 發布成靜態網站

## 投影片 12（來源：wiki/synthesis-failures.md、wiki/overview.md、wiki/source-06-awesome.md）
總結
- 常見失敗：近重複頁 → Extend, don't create；斷連結 → 程式 lint；靜默覆蓋矛盾 → 並列標注
- 一句話帶走：知識要編譯一次、持續維護，而不是每次重新推導
- gist 發布後數個月，生態清單（Awesome LLM Wiki）已經成型
