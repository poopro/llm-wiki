---
type: entity
tags: [研究, 成本]
sources: [raw/05-crow-llm-wiki-v2.md]
updated: 2026-11-16
---

# 實體：CROW llm-wiki-v2（ingest 決策成本研究）

GitHub 專案 `crow-hq/llm-wiki-v2`（AGPL-3.0，可用 Ollama 本地模型）：針對 ingest 環節做了一次量化研究 [[entity-karpathy]]。

**發現**：ingest 時大多數 LLM 呼叫其實不是在「寫」，而是在「決策」——這份資料歸哪個資料夾？是否與既有筆記同一主題？要不要合併？該連到哪裡？**這些決策佔了約 72% 的 LLM token**。

**對策**：把這些決策交給小型 typed classifier，LLM 只負責產生文字內容。

**結果**（525 份文件的單一語料、單一模型）：正確筆記被送到答案的比例從 62% 提升到 89%，ingest 時間約減半，且每份文件的 token 成本在 wiki 變大時保持平坦。作者自己註明「單一語料、單一模型，只能當作第一個數據點」。

對本 wiki 的啟示：**結構化、可程式化的檢查與分類，能大幅降低維護成本**——與 [[entity-mindbase]] 的「lint 用程式算、不用模型」互相呼應。來源摘要頁：[[source-05-crow]]

出處：raw/05-crow-llm-wiki-v2.md
