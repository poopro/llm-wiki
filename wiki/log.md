# Log — 操作日誌（append-only）

## [2026-11-16] setup | 依「先討論、後生成」建立 wiki

- 完成 9 題需求訪談（notes/requirements-discussion.md），使用者確認需求摘要。
- 生成 AGENTS.md（schema）與資料夾結構；逐條對照：讀者、頁面類型、語言、出處格式、矛盾處理、ingest 節奏、下游產出、lint 項目皆已寫入手冊。

## [2026-11-16] ingest | 01 Karpathy — LLM Wiki gist（原典）

- 新增：raw/01、wiki/source-01-karpathy、wiki/entity-karpathy
- 更新：concept-compilation、concept-three-layers、concept-operations、concept-index-log、overview
- 備註：gist 留言區的社群經驗（extend don't create 等）單獨記住，等 lint 頁面建立時併入。

## [2026-11-16] ingest | 02 IssacW228 — student-llm-wiki

- 新增：raw/02、wiki/source-02-student、wiki/entity-student-llm-wiki
- 更新：overview

## [2026-11-16] ingest | 03 frankchu91 — mindbase-llm-wiki

- 新增：raw/03、wiki/source-03-mindbase、wiki/entity-mindbase
- 更新：concept-operations（lint 程式化）、concept-index-log（查詢日誌）、synthesis-failures

## [2026-11-16] ingest | 04 liangdabiao — llm-wiki（多來源、Quartz）

- 新增：raw/04、wiki/source-04-liangdabiao、wiki/entity-liangdabiao
- 更新：overview

## [2026-11-16] ingest | 05 crow-hq — llm-wiki-v2（決策成本研究）

- 新增：raw/05、wiki/source-05-crow、wiki/entity-crow
- 更新：comparison-vs-rag（成本曲線列）、synthesis-failures（對策 #6）

## [2026-11-16] ingest | 06 gavischneider — awesome-llm-wiki

- 新增：raw/06、wiki/source-06-awesome
- 更新：index（source 分類補完）
- 備註：清單型來源，不另建 concept；四個代表專案已各有實體頁。

## [2026-11-16] lint | 第 1 次全庫 lint（scripts/wiki_lint.py）

- 發現 61 個問題，其中真實內容問題只有 6 個（孤兒頁：source-01～06 沒被任何內容頁連結）。
- 其餘 55 個是 lint 腳本自己的 bug 誤報：①findall 回傳含 raw/ 前綴的 match，拼出路徑 raw/raw/... 判定全部出處不存在（52 個壞引用）；②行內程式碼裡的 [[wikilink]]、[[link]] 被當成真連結（3 個斷連結）。
- 教訓：檢查腳本本身也要被檢查；第 1 輪先修腳本，再修內容。

## [2026-11-16] lint | 第 2 次全庫 lint

- 修復：腳本剝前綴＋掃描前移除行內程式碼；entity 頁補上來源摘要頁連結、overview 補 [[source-06-awesome]]。
- 結果：全過（18 頁、6 來源：無斷連結、無孤兒頁、每頁有出處、index 收錄完整）。

## [2026-11-16] query | 檢索 wiki 做教學簡報

- 依「教會不熟悉主題的人」目標，從 index.md 選出 12 頁（topic-llm-wiki-slides/sources.md）。
- 覆蓋率關卡：12 頁 ≥ 3 頁門檻 → 通過。

## [2026-11-16] slides | 大綱 → 逐頁稿 → deck.html

- 6 張證據卡（每張只看一篇 raw 來源）→ outline.md（12 頁，人工確認）→ drafts/slides-v1.md → deck.html。
- 程式檢查 deck_check.py：12 頁、引用 13 個 wiki 頁、每頁有出處 → 全過。
- 瀏覽器渲染檢查：12 頁無溢出（1000×700；內容底端皆 < 視窗 98%）。
- 忠實度審查：三個關鍵數字（72%、62%→89%、10–15 頁）對回 raw 原文，限制語保留。
- 全部關卡通過，依停止條件停止。紀錄見 topic-llm-wiki-slides/report.md。

## [2026-11-18] build | wiki → 靜態網站（scripts/build_site.py）

- 新增 scripts/build_site.py：wiki/ 每頁渲染成 site/<slug>.html，根目錄 index.html 變成總覽目錄（分類卡片 + 簡報連結）。
- AGENTS.md 新增「網站生成」章節：生成物不可手改；新增頁面的閉環 = ingest → lint → build_site → commit → Pages 自動上線。
- 驗證：site/ 共 20 頁、無殘留 [[wikilink]]、站內連結轉換正確。

