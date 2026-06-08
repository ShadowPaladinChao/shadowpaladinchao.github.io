---
name: stock-exploration-to-web
description: '股票数据探索 → 报告 → 网页全流程。Use when: 对一只股票做数据探索、生成量化分析报告、将报告转为Vue页面展示。涵盖Python数据拉取(baostock/akshare)、图表生成、markdown报告撰写、以及用NoteDetail.vue将报告转成前端页面。'
argument-hint: '股票代码 或 "数据探索"、"量化报告"、"转网页"'
---

# 股票数据探索 → Web 页面 全流程

将一只股票的数据探索做成网页展示的端到端工作流。

## When to Use

- 用户说"探索某只股票"、"做数据探索"、"生成分析报告"
- 用户说"把这个报告放到网页上"、"生成一个页面"
- 涉及 baostock/akshare 数据 + matplotlib 图表 + Vue 页面的组合

## 整体流程

```
数据拉取 → 数据分析 → 图表生成 → Markdown报告 → Vue页面
(explore_stock.py)                  (report.md)    (NoteDetail.vue)
```

## Procedure

### Step 1: 创建规划文档

先写一个规划文档（可复用 `plan-doc` skill）描述：
- 标的代码/名称
- 数据范围（近2年）
- 数据来源（baostock / akshare）
- 产出物清单

模板参考 `ycquant/docs/stock-data-exploration.md`。

### Step 2: 数据拉取与分析（Python）

使用参数化的 `explore_stock.py`，接受**股票代码**和**名称**作为命令行参数：

```bash
# 基本用法（默认拉取近2年）
conda run -n quant python ycquant/scripts/explore_stock.py <代码> <名称>

# 指定日期范围
conda run -n quant python ycquant/scripts/explore_stock.py <代码> <名称> 2023-01-01 2025-12-31

# 示例
conda run -n quant python ycquant/scripts/explore_stock.py sz.002851 麦格米特
conda run -n quant python ycquant/scripts/explore_stock.py sh.600879 航天电子
```

脚本自动完成：
- 公司基本信息 + 行业分类
- 近N年日线数据（OHLCV + PE/PB/PS/PCF + 换手率 + 涨跌幅）
- 季度财报（营收/净利/毛利率/净利率/ROE/负债率）
- 15 张图表生成到 `ycquant/research/<代码>-<名称>/exploration-<日期>/`
- 数据存储为 parquet 到 `ycquant/data/raw/stock/`

### Step 3: 图表生成

生成的图表放在 `ycquant/research/<股票代码-名称>/exploration-YYYYMMDD/` 下：

| 图表 | 文件名 | 内容 |
|------|--------|------|
| 价格走势 | `explore_price.png` | K线/收盘价 + MA20/MA60/MA120 |
| 成交量 | `explore_volume.png` | 成交量柱 + 换手率线（双Y轴） |
| PE走势 | `explore_pe.png` | PE(TTM) + 分位标记 |
| PB走势 | `explore_pb.png` | PB(MRQ) + 分位标记 |
| PCF走势 | `explore_pcf.png` | PCF(NcfTTM) |
| 估值全景 | `explore_valuation.png` | PE/PB/PS 归一化至中位数=1 |
| 指标分布 | `explore_dist.png` | PE/PB/换手率/涨跌幅的概率密度 |
| 季度财务×6 | `explore_quarterly_*.png` | 营收/净利/毛利率/净利率/ROE/负债率 |

### Step 4: 生成报告

自动生成 `report.md`，要求：
- 标题：`股票名称 数据探索报告（最新数据日期）`
- 每个估值指标解释含义 + 当前值 + 历史分位
- 每张图下方写基于实际数据的解读（不要说明书）
- 统计摘要表 + 解读
- 总结表
- 免责声明

### Step 5: 转为 Vue 页面

#### 5.1 确保 junction 已建立（一次性操作）

`public/research/` 通过 NTFS junction 映射到 `ycquant/research/`，图片零冗余自动可用：

```powershell
# 一次性创建（若不存在）
if (-not (Test-Path public\research)) {
    New-Item -ItemType Junction -Path public\research `
        -Target "D:\YaoChaoFiles\WorkSpace\shadowpaladinchao.github.io\ycquant\research"
}
```

之后每次跑完脚本，图片自动通过 `/research/<代码>-<名称>/exploration-<日期>/` 路径可访问。

#### 5.2 在 Projects.vue 添加列表条目

```ts
const articles: any[] = [
  {
    slug: 'stock-600879',
    emoji: '🚀',
    title: '航天电子 数据探索报告',
    date: '2026-06-09',
    summary: '近2年数据全景探索...',
    tags: ['量化分析', '数据探索', '航天军工'],
  },
]
```

#### 5.3 在 NoteDetail.vue 添加文章数据

数据放在 `articles` 对象的对应 slug key 下，结构如下：

```ts
{
  title: '股票名称 数据探索报告',
  subhead: '数据区间 YYYY-MM-DD ~ YYYY-MM-DD（N 个交易日）· 来源 baostock（前复权）',
  date: 'YYYY-MM-DD',
  emoji: '🚀',
  tags: ['量化分析', '数据探索', '行业标签'],
  sections: [
    // 每类 section 支持 ↓
  ],
  disclaimer: '免责声明',
}
```

#### 5.4 Section 类型

NoteDetail.vue 支持 5 种 section 类型，按数据顺序从上到下排列：

| 类型 | 关键字段 | 用途 |
|------|---------|------|
| `cards` | `{ label, value, sub?, color? }[]` | 基本信息、行情数据、表现概览 |
| `table` | `{ headers, rows }` | 估值表、统计摘要 |
| `content` + `image` + `imageNote` | 文本 + 单张全宽图 | 图表区段（每个图一个 section） |
| `summary` | `{ label, value }[]` | 最终总结 |
| 纯 `content` | 文本段落 | 任意说明文字 |

**重要规则**：
- `content`（解析文字）必须放在 `cards`/`table`/`image` **之前**，作为引导说明
- 每个图表单独一个 section，不要合并在 grid 中
- section 顺序 = 报告中的章节顺序
- 文本内容要有深度，结合具体数字做解读，不要写"怎么看图"的说明书

#### 5.5 页面布局

```html
<div class="min-h-screen pt-24 pb-16 px-6 sm:px-10 lg:px-14 text-left">
  <!-- 无 max-w 限制，全宽布局 -->
  <!-- 返回按钮 -->
  <!-- 文章头部（标题左对齐） -->
  <!-- sections 按序渲染 -->
</div>
```

关键 CSS：
- 无 `max-w-*` 限制，让内容撑满页面
- `text-left` 显式声明左对齐
- `<main>` 在 App.vue 中也需要 `text-left`
- section 标题用 `border-l-4 border-purple-500 pl-3` 左对齐紫色竖线

## 数据字段参考

baostock 日线接口可获取字段：

| 字段 | 含义 | 类型 |
|------|------|------|
| date | 日期 | str |
| open/high/low/close | OHLC（前复权） | float |
| volume | 成交量（股） | int |
| amount | 成交额（元） | float |
| turn | 换手率（%） | float |
| pctChg | 涨跌幅（%） | float |
| peTTM | 市盈率 | float |
| pbMRQ | 市净率 | float |
| psTTM | 市销率 | float |
| pcfNcfTTM | 市现率 | float |

## 输出文件结构

```
public/research/                         # → junction → ycquant/research/（零冗余）
  <代码>-<名称>/
    exploration-YYYYMMDD/
      explore_*.png                      # 前端直接通过 /research/ 路径访问

src/pages/
  Projects.vue                           # 笔记列表页（添加条目）
  NoteDetail.vue                         # 笔记详情页（添加文章数据）

ycquant/research/<代码>-<名称>/
  exploration-YYYYMMDD/
    report.md                            # Markdown 报告
    explore_*.png                        # 原始图表

ycquant/data/raw/stock/
  <代码>.parquet                         # 原始数据
```
