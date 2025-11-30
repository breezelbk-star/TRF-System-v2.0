# TRF-System v2.0 — Core Index（内核目录 · 最终版）

本文件作为 TRF 系统 **总入口（Index）**，指向所有核心模块文件。  
所有正式规则、风控逻辑、执行规则均在对应文件中维护。

> 说明：本文件只做“导航”和“结构说明”，不写规则本身。

---

# 🧩 0. TRF v2.0 的结构（总览）

TRF 内核由三大系统组成：

1. **Trend（趋势）**  
2. **Rotation（轮动）**  
3. **Flow（资金）**  

并由三个辅助系统补充：

4. **Risk（三色灯风控）**  
5. **Execution（日内执行流程）**  
6. **My-Style-Model（交易人格模型）**

此外还有“辅助库”  
- 环境判定规则  
- 每日 Playbook（Morning / 10:00 / 11:30 / 13:45 / Close / Night）  
- 案例库（成功 & 失败）  
- 单股关键位（Key-Levels）

---

# 🏛 1. 内核模块（Core Modules · 只在大版本升级时修改）

内核模块都位于 `/TRF-Core/` 目录：

| 文件 | 内容 |
|------|------|
| **1.1-Trend.md** | 大盘 / 板块 / 个股趋势标准，多头 / 震荡 / 防守结构 |
| **1.2-Rotation.md** | 主线判定、四类仓位（Core/Attack/Defensive/Test）、轮动规则 |
| **1.3-Flow.md** | 资金强弱、量价关系、有效突破 vs 假突破 |
| **1.4-Risk.md** | 红黄绿灯、仓位限制、止盈/止损、系统优先级 |
| **1.5-Execution.md** | 盘前 → 10:00 → 11:30 → 13:45 → 收盘 的执行流程 |

---

# 🟩 2. 系统优先级（必须写清楚 · 避免未来冲突）

TRF 系统的判断优先级如下：

```
风险灯（Risk）  >  趋势（Trend）  >  轮动（Rotation）  >  资金（Flow）  >  临盘（Execution）
```

> 解释：  
> - Risk = 总开关（决定当天能做什么）  
> - Trend = 大方向（多头 / 震荡 / 防守）  
> - Rotation = 资金在哪 → 仓位放哪  
> - Flow = 当下突破是真还是假  
> - Execution = 把上面四个拆成日内动作  

🔔 **一切以 Risk + 环境红黄绿灯 为最高优先级。**

---

# 🧭 3. 目录结构（当前 GitHub 已实现 · 与仓库同步）

以下是你仓库的实际结构（已校准）：

```
TRF-System-v2.0/
│
├── 0.0-TRF-Core-1.1.md   ←（本文件）
│
├── TRF-Core/
│     ├── 1.1-Trend.md
│     ├── 1.2-Rotation.md
│     ├── 1.3-Flow.md
│     ├── 1.4-Risk.md
│     └── 1.5-Execution.md
│
├── docs/
│     ├── 00_environment_rules.md
│     ├── Daily-Playbook/
│     │       ├── 08-30_Morning-Playbook.md
│     │       ├── 10-00_Check.md
│     │       ├── 11-30_Midday-Review.md
│     │       ├── 13-45_Afternoon-Check.md
│     │       ├── 15-00_Close-Review.md
│     │       └── Night-Playbook.md
│     │
│     ├── My-Style-Model v1.1.md
│     └── cases/
│             ├── Case-01_NorthRareEarth.md
│             ├── Case-02_Sungrow.md
│             ├── Case-03_Qiaoyuan.md
│             └── Case-04_ChinaGreatWall.md
│
└── Key-Levels/     （若未来加入每只股票的关键价位文件）
```

---

# 🎭 4. 角色体系统一说明（Core / Attack / Defensive / Test）

系统最终统一使用**四类主角色**：

| 角色 | 定义 |
|------|------|
| **Core（核心龙头）** | 主线最强、最纯、可中期持有 |
| **Attack（进攻仓）** | 主升浪二线补涨 / 加速突破 |
| **Defensive（防御）** | 高股息 / 电力 / 稳健仓位（仅黄灯/红灯时用） |
| **Test（试错）** | 小仓验证新风口（3–5%） |

子标签（用于辅助识别）：

- AR（Attack-Relay）= 二线补涨  
- AC（Attack-Acceleration）= 加速突破  
- Side = 非主线  
- Risk = 风险标记  

---

# 📚 5. 内核 vs 应用层（如何区分？）

**内核（Core）**：  
- Trend  
- Rotation  
- Flow  
- Risk  
- Execution  
- My-Style-Model  

这些文件属于“冻结规则”，除非大改，否则不调整。

**应用层（Docs）**：  
- 环境规则  
- 所有 Playbook  
- 案例库  
- 单股关键价位  

这些文件可以在实盘中不断增加和补充。

---

# ✔ 6. 版本说明

本文件为 TRF v2.0 的目录与结构定义。  
若未来内核升级为 v2.1 / v3.0，本文件需同步更新。
