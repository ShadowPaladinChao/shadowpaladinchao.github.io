# Stock Data Exploration

> 日期：2026-06-09
> 状态：进行中
> 标的：航天电子（sh.600879）
> 数据范围：2024-06-09 ~ 2026-06-09（近2年）

---

## 1. 目的（Purpose）

- 对**航天电子（sh.600879）**做一次全面的数据拉取与展示
- 时间范围：**近2年（2024-06-09 ~ 2026-06-09）**
- 尽可能多地获取与公司相关的数值：价格、成交量、换手率、PE、PB、PS、PCF、市值等
- **不做收益分析、不做策略回测**，纯粹「看数据」
- 最终生成一份**详细的数据探索报告**，每个指标、每张图都有解释

## 2. 背景（Background）

- ycquant 环境就绪，baostock 可用
- baostock 日线接口支持字段：`date, open, high, low, close, preclose, volume, amount, adjustflag, turn, tradestatus, pctChg, peTTM, pbMRQ, psTTM, pcfNcfTTM, isST`
- 可通过 `query_stock_basic` 获取公司基本信息，`query_stock_industry` 获取行业分类

## 3. 方法（Method）

| 数据维度 | 来源 | 字段 |
|----------|------|------|
| 公司基本信息 | baostock `query_stock_basic` | 代码、名称、上市日期、类型、状态 |
| 行业分类 | baostock `query_stock_industry` | 行业类别 |
| 日线行情 | baostock `query_history_k_data_plus` | OHLCV + 换手率 |
| 估值指标 | 同上接口 | peTTM、pbMRQ、psTTM、pcfNcfTTM |
| 涨跌幅 | 同上接口 | pctChg（涨跌幅%） |

## 4. 流程（Process）

1. **拉取数据**
   - 公司基本信息 + 行业分类
   - 近2年日线，含所有 baostock 支持的字段
   - 保存到 `data/raw/stock/sh_600879.parquet`

2. **数据概览**
   - 基本信息打印（含行业）
   - 数据规模（行数、日期范围）
   - 各字段统计摘要
   - 缺失值检查

3. **可视化**
   - 图1：价格走势 + MA20/MA60/MA120 均线
   - 图2：成交量 + 换手率（双Y轴）
   - 图3：PE(TTM) 历史走势 + 分位
   - 图4：PB(MRQ) 历史走势 + 分位
   - 图5：PE/PB/PS 估值全景（归一化对比）
   - 图6：PE、PB、换手率、涨跌幅分布

4. **生成报告**（报告要求如下）

### 报告详细要求

#### 报告格式
- 标题格式：`股票名称 数据探索报告（最新数据日期）`，如 `航天电子 数据探索报告（2026-06-08）`
- 不要用 "report" 作为标题
- 包含代码、名称、上市日期、上市年限、行业分类
- 解释 type/status 字段含义

#### 估值指标解释
- PE(TTM)：市盈率，股价/每股收益，衡量盈利能力
- PB(MRQ)：市净率，股价/每股净资产，衡量资产价值
- PS(TTM)：市销率，总市值/营业收入，衡量收入规模
- PCF(NcfTTM)：市现率，股价/每股现金流，衡量现金创造能力
- 每个指标说明高/低的含义

#### 统计摘要
- 每列指标必须加注释说明是什么
- 对关键数值做解读（如 PE 中位数 vs 当前值的含义）

#### 每张图表
- 图下方必须有**基于实际数据的解读**，而不是"怎么看这张图"的说明书
- 解读要结合具体数值：最高点日期和价格、当前相对均线的位置、成交量放大/缩小趋势等
- 用具体数字说话（"PE从47涨到533" 而不是 "PE波动较大"）

## 5. 预期产出（Deliverables）

- [x] `scripts/explore_stock.py` — 拉取 + 分析 + 出图 + 报告 一体化
- [x] `output/explore_price.png` — 价格走势 + 均线
- [x] `output/explore_volume.png` — 成交量 + 换手率
- [x] `output/explore_pe.png` — PE 走势 + 分位
- [x] `output/explore_pb.png` — PB 走势 + 分位
- [x] `output/explore_valuation.png` — PE+PB+PS 估值全景
- [x] `output/explore_dist.png` — 指标分布
- [ ] `research/stock-exploration/report.md` — **详细**完整报告（需重写）
- [ ] `skills/stock-exploration/SKILL.md` — 固化为 skill

## 6. 风险 & 备注（Risks & Notes）

- baostock 速度慢，耐心等待
- PE/PB/PS/PCF 可能有缺失值（停牌日），出图前 fillna
- 不做收益分析、不做策略，只看数据本身
- 报告要详细：每个指标有解释，每张图有解读
