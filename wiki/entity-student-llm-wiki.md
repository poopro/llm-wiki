---
type: entity
tags: [實作, 教育]
sources: [raw/02-student-llm-wiki.md]
updated: 2026-11-16
---

# 實體：Student LLM Wiki（學生課程知識庫）

GitHub 專案 `IssacW228/student-llm-wiki`（2026-06 建立，MIT 授權）：把上課簡報丟進去，AI 編譯成持久、互連的課程 wiki [[entity-karpathy]]。

特色：

- **Feynman 複習**、考古題練習、信心衰減（confidence decay）追蹤、跨課程連結
- 流程：上傳課程簡報 → 在 `wiki/` 產生結構化筆記 → 用 Obsidian 瀏覽 → AI 協助複習、出題、標出弱點
- 明確標示「Based on Karpathy's LLM Wiki pattern」，搭配 Claude Code / Claude Cowork 運作

這是「課程筆記」情境的代表性實作：知識庫的主人（學生）負責上傳與複習，LLM 負責整理與維護 [[concept-compilation]]。來源摘要頁：[[source-02-student]]

出處：raw/02-student-llm-wiki.md
