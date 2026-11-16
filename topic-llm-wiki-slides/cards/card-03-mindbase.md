# 證據卡 03 — mindbase-llm-wiki

**節點權限：只看 raw/03-mindbase-llm-wiki.md，不混入其他來源。**

可用的關鍵主張：
1. 斷引用（cited 檔案被移走/刪除）與斷連結（[[wikilink]] 沒有頁面）在 lint 時**由程式計算**，不經模型 → 沒有誤報。
2. 近重複偵測：「extend, don't create」——提示維護者擴充既有頁而不是再建一頁。
3. 上下文預算透明化：回答回報「read 3 pages · 9.1k of 14.2k chars fit · clipped: deep-work.md」，靜默丟資料變得可見。
4. 查詢日誌記錄「讀了哪幾頁 vs 引用了哪幾頁」，「wiki 有、模型沒用」可以事後 grep。

餵給投影片：7、8、11
