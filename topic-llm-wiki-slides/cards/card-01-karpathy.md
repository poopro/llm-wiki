# 證據卡 01 — Karpathy gist（原典）

**節點權限：只看 raw/01-karpathy-llm-wiki-gist.md，不混入其他來源。**

可用的關鍵主張：
1. RAG 模式：LLM 每次回答都「從頭重新發現知識」，沒有累積。
2. 核心句：「知識被編譯一次然後保持更新，而不是每次查詢重新推導。」
3. 三層架構：raw/ 不可修改（source of truth）、wiki/ 由 LLM 全權維護、schema（AGENTS.md）規範行為。
4. Ingest 標準流程：讀→討論→摘要頁→更新 index→更新相關頁→記 log；**一份來源可能碰 10–15 頁**。
5. Query：先讀 index 找頁面再深入；好答案回寫成新頁。
6. Lint：矛盾、過時主張、孤兒頁、缺頁、缺交叉引用、資料缺口。
7. index.md ≈ 百頁規模內可取代 embedding 檢索；log.md 固定前綴可用 grep 解析。
8. 思想來源：Vannevar Bush 的 Memex（1945）；Karpathy 補上「誰來維護」的答案 = LLM。
9. 技巧：Obsidian graph view、Marp 直接從 wiki 產投影片、整個 wiki 是 git repo。

餵給投影片：6（主要）、2、3、4、5、7、9
