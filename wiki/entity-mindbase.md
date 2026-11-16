---
type: entity
tags: [實作, 工具化]
sources: [raw/03-mindbase-llm-wiki.md]
updated: 2026-11-16
---

# 實體：MindBase（把 wiki 維護程式化）

GitHub 專案 `frankchu91/mindbase-llm-wiki`（npm 套件 mindbase-mcp）：把 Karpathy 的模式做成產品，特色是**把 lint 從「請 AI 檢查」變成「程式碼計算」** [[concept-operations]]：

- **斷引用（broken citation）**：頁面引用的 `[@path]` 指向被移動或刪除的檔案
- **斷連結（broken link）**：`[[wikilink]]` 背後沒有頁面或筆記
- 兩者都在 lint 時由程式算出，「No model involved, so no false 'I think this might be missing'」——不經模型判斷，就不會有誤報
- **近重複偵測**：找出研究同一概念、名字相近的頁面，提示維護者「擴充它而不是再建一頁」（extend, don't create）[[synthesis-failures]]
- **上下文預算透明化**：組裝器若丟掉超過預算的內容，每次回答都回報一行，例如「read 3 pages · 9.1k of 14.2k chars fit · clipped: deep-work.md」，讓「靜默丟資料」變得可見
- **查詢日誌**：記錄讀了哪幾頁 vs 引用了哪幾頁 [[concept-index-log]]

來源摘要頁：[[source-03-mindbase]]

出處：raw/03-mindbase-llm-wiki.md
