"""数据可视化测试
基于已拉取的股票数据，绘制 K线图、走势对比、成交量等测试图表。
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from data.storage import load_raw

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "Arial"]
plt.rcParams["axes.unicode_minus"] = False

# ============ 加载数据 ============
STOCKS = {
    "sh_600519": "贵州茅台",
    "sz_000001": "平安银行",
    "sz_000002": "万科A",
}

data = {}
for code, name in STOCKS.items():
    df = load_raw(code)
    if df is not None:
        data[code] = df
        print(f"{name} ({code}): {len(df)} 条")

if not data:
    print("没有数据，请先运行 scripts/fetch_test.py")
    exit(1)

# ============ 图1: 收盘价走势对比 ============
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("ycquant 股票数据可视化测试", fontsize=16, fontweight="bold")

# 1.1 收盘价走势
ax1 = axes[0, 0]
for code, name in STOCKS.items():
    if code in data:
        # 归一化到 1.0 起点
        norm = data[code]["close"] / data[code]["close"].iloc[0]
        ax1.plot(data[code].index, norm, label=name, linewidth=1.2)
ax1.set_title("归一化收盘价走势（起点=1.0）")
ax1.legend(loc="best", fontsize=8)
ax1.axhline(y=1.0, color="gray", linestyle="--", alpha=0.5)
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
ax1.tick_params(axis="x", rotation=30)
ax1.grid(True, alpha=0.3)

# 1.2 贵州茅台 K线图（最近60天）
ax2 = axes[0, 1]
df_mt = data.get("sh_600519")
if df_mt is not None:
    recent = df_mt.tail(60)
    colors = ["red" if recent["close"].iloc[i] >= recent["open"].iloc[i] else "green"
              for i in range(len(recent))]
    x = range(len(recent))
    ax2.bar(x, recent["high"] - recent["low"], bottom=recent["low"],
            color=colors, width=0.6, alpha=0.8, linewidth=0)
    ax2.bar(x, abs(recent["close"] - recent["open"]),
            bottom=recent[["open", "close"]].min(axis=1),
            color=colors, width=0.3)
    # 标注日期
    ticks = list(range(0, len(recent), 10))
    ax2.set_xticks(ticks)
    ax2.set_xticklabels([recent.index[i].strftime("%m-%d") for i in ticks])
    ax2.set_title(f"贵州茅台 K线图（近{len(recent)}日）")
    ax2.grid(True, alpha=0.3)

# 2.1 收益率分布直方图
ax3 = axes[1, 0]
for code, name in STOCKS.items():
    if code in data:
        returns = data[code]["pctChg"].dropna()
        ax3.hist(returns, bins=50, alpha=0.5, label=name, density=True)
ax3.set_title("日涨跌幅分布")
ax3.legend(fontsize=8)
ax3.axvline(x=0, color="gray", linestyle="--", alpha=0.5)
ax3.grid(True, alpha=0.3)

# 2.2 成交量对比（归一化）
ax4 = axes[1, 1]
for code, name in STOCKS.items():
    if code in data:
        vol_norm = data[code]["volume"] / data[code]["volume"].max()
        ax4.fill_between(data[code].index, 0, vol_norm, label=name, alpha=0.4, linewidth=0.5)
ax4.set_title("成交量对比（归一化）")
ax4.legend(fontsize=8)
ax4.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
ax4.tick_params(axis="x", rotation=30)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
outpath = Path(__file__).resolve().parent.parent / "output" / "test_charts.png"
plt.savefig(outpath, dpi=150, bbox_inches="tight")
print(f"\n图表已保存: {outpath}")
plt.show()
