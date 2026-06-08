"""个股 K线图 + 均线
为每只股票单独生成一张 K线图，叠加 5/20/60/120 日均线。
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle
from data.storage import load_raw

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "Arial"]
plt.rcParams["axes.unicode_minus"] = False

# ============ 配置 ============
STOCKS = {
    "sh_600519": "贵州茅台",
    "sz_000001": "平安银行",
    "sz_000002": "万科A",
}
MA_PERIODS = [5, 20, 60, 120]       # 均线周期
MA_COLORS  = ["#FF6B6B", "#4ECDC4", "#FFD93D", "#6C5CE7"]  # 均线颜色
SHOW_DAYS  = 180                     # 显示最近多少天
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


def draw_kline_with_ma(df: pd.DataFrame, name: str, code: str):
    """绘制单只股票的 K线图 + 均线"""
    df = df.tail(SHOW_DAYS).copy()

    # 计算均线
    for p in MA_PERIODS:
        df[f"MA{p}"] = df["close"].rolling(p).mean()

    fig, (ax_top, ax_bot) = plt.subplots(
        2, 1, figsize=(16, 9),
        gridspec_kw={"height_ratios": [4, 1], "hspace": 0.05},
        sharex=True
    )
    fig.suptitle(f"{name}（{code}）K线图 + 均线", fontsize=18, fontweight="bold", y=0.96)

    # ---- 上部: K线 ----
    width = 0.6
    for i, (idx, row) in enumerate(df.iterrows()):
        color = "#e74c3c" if row["close"] >= row["open"] else "#2ecc71"  # 红涨绿跌

        # 影线（最高-最低）
        ax_top.plot([i, i], [row["low"], row["high"]], color=color, linewidth=0.8)

        # 实体（开盘-收盘）
        body_bottom = min(row["open"], row["close"])
        body_height = abs(row["close"] - row["open"]) or 0.01  # 十字星显示为一根线
        ax_top.add_patch(Rectangle(
            (i - width / 2, body_bottom), width, body_height,
            facecolor=color, edgecolor=color, linewidth=0.5, alpha=0.9
        ))

    # 均线
    for p, c in zip(MA_PERIODS, MA_COLORS):
        ax_top.plot(range(len(df)), df[f"MA{p}"], color=c, linewidth=1.0,
                    label=f"MA{p}", alpha=0.85)

    ax_top.legend(loc="upper left", fontsize=9, ncol=4, framealpha=0.8)
    ax_top.set_ylabel("价格（前复权）", fontsize=11)
    ax_top.grid(True, alpha=0.25, linestyle="--")

    # 标注最新价格
    last_price = df["close"].iloc[-1]
    ax_top.axhline(y=last_price, color="gray", linestyle=":", alpha=0.5, linewidth=0.8)

    # ---- 下部: 成交量 ----
    for i, (idx, row) in enumerate(df.iterrows()):
        color = "#e74c3c" if row["close"] >= row["open"] else "#2ecc71"
        ax_bot.bar(i, row["volume"], color=color, width=0.6, alpha=0.6, linewidth=0)

    ax_bot.set_ylabel("成交量", fontsize=10)
    ax_bot.grid(True, alpha=0.25, linestyle="--")

    # X轴日期标注
    step = max(1, len(df) // 8)
    tick_idx = list(range(0, len(df), step))
    tick_labels = [df.index[i].strftime("%Y-%m-%d") for i in tick_idx]
    ax_bot.set_xticks(tick_idx)
    ax_bot.set_xticklabels(tick_labels, rotation=30, ha="right", fontsize=8)

    # 保存
    outpath = OUTPUT_DIR / f"kline_{code}.png"
    plt.savefig(outpath, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  ✅ {outpath.name}")


def main():
    print("=" * 50)
    print("生成个股 K线图 + 均线")
    print("=" * 50)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for code, name in STOCKS.items():
        df = load_raw(code)
        if df is None:
            print(f"  ❌ {name}: 无数据，请先运行 scripts/fetch_test.py")
            continue
        print(f"\n📊 {name} ({code}) — {len(df.tail(SHOW_DAYS))} 条")
        draw_kline_with_ma(df, name, code)

    print(f"\n图表保存在: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
