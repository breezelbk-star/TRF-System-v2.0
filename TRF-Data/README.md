# TRF-Data

TRF-System 的数据构建层。

## Responsibilities
- 从公开数据源（akshare）获取 A 股行情
- 统一使用前复权（QFQ）价格
- 计算 TRF 系统所需的基础指标（MA20 / 60 / 120 / 250）
- 输出为 CSV，供 TRF-Engine 使用

## Notes
- 数据文件不纳入 Git 管理
- 实盘价格请以交易软件为准
