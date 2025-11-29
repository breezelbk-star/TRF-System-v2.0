# TRF-System-v2.0（半导体主线版）
This repository contains Jimmy 的私人交易体系：  
**TRF = Trend（趋势） + Rotation（轮动） + Flow（资金）**

本仓库用于存放所有固定逻辑、操作流程、关键位模板、个股评分模型等内容。  
每日的实盘分析仍然由 ChatGPT 根据截图执行，GitHub 主要保存**永不改变的“内核”**。

---

## 🧩 仓库结构
```
TRF-System-v2.0/
│
├── README.md
│
├── docs/
│   ├── TRF-Core.md
│   ├── Daily-Playbook.md
│   ├── Key-Levels-Template.md
│   └── Stock-Rating-Model.md
│
└── examples/
    ├── Example-Playbook.md
    └── Example-Stock-Rating.md
```

---

## 🔥 核心思想：固定内核 + 变量实时由 AI 计算

GitHub 中只存放以下内容：
1. **固定不会改变的内核逻辑**
2. **你的操作标准（盘前、盘中、盘后）**
3. **每只股票的“评分维度”与“关键位模板”**

所有实时数据（股价、五档、资金、走势）由 ChatGPT 在你发送截图时执行。

---

## 📌 项目目标
- 让交易风格有统一标准  
- 让 ChatGPT 每天的盘前、盘中、盘后分析更稳定  
- 不需要频繁更新 GitHub，只更新“永恒逻辑”

---
