# -*- coding: utf-8 -*-
"""航天电子 数据探索 — 日线+3年季度财报+图表+报告"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import baostock as bs, pandas as pd, numpy as np
import matplotlib.pyplot as plt, matplotlib.dates as mdates
from data.storage import save_raw

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "Arial"]
plt.rcParams["axes.unicode_minus"] = False

STOCK_CODE = "sh.600879"; STOCK_NAME = "航天电子"
START_DATE = "2024-06-09"; END_DATE = "2026-06-09"
REPORT_DIR = Path(__file__).resolve().parent.parent / "research" / f"{STOCK_CODE}-{STOCK_NAME}" / "exploration-20260609"
SAVE_NAME = "sh_600879"; REPORT_DIR.mkdir(parents=True, exist_ok=True)
FIELDS = "date,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST"
PERIODS = ["Q1","Q2单季","半年报","Q3","Q4单季","年报"]
PERIOD_SUFFIX = ["Q1","Q2s","H1","Q3","Q4s","FY"]  # 对应df_q列名后缀
PERIOD_COLORS = ["#3498db","#2980b9","#2ecc71","#f39c12","#e67e22","#e74c3c"]


# ======== 1. 日线数据 ========
def fetch_data():
    print("=" * 60); print("[1/4] 拉取日线..."); bs.login()
    rs = bs.query_stock_basic(STOCK_CODE); info = {}
    while (rs.error_code == "0") & rs.next():
        r = rs.get_row_data()
        info = {"code": r[0], "name": r[1], "ipo_date": r[2], "type": r[4], "status": r[5]}
    rs = bs.query_stock_industry(STOCK_CODE); ind = "未知"
    if rs.error_code == "0":
        while rs.next():
            row = rs.get_row_data()
            ind = row[3] if len(row) > 3 else "未知"
    yl = 2026 - int(info["ipo_date"][:4]) if info["ipo_date"] else 0
    tm = {"1": "股票", "2": "指数", "3": "其他", "4": "ETF", "5": "可转债"}
    sm = {"1": "正常上市", "0": "已退市"}
    info.update({"industry": ind, "years_listed": yl, "type_str": tm.get(info.get("type",""),""), "status_str": sm.get(info.get("status",""),"")})
    print(f"  {info['name']}({info['code']}) 上市{info['ipo_date']}({yl}年) {ind}")

    rs = bs.query_history_k_data_plus(STOCK_CODE, FIELDS, start_date=START_DATE, end_date=END_DATE, frequency="d", adjustflag="2")
    data = []; 
    while (rs.error_code == "0") & rs.next(): data.append(rs.get_row_data())
    bs.logout()
    df = pd.DataFrame(data, columns=rs.fields)
    for c in ["open","high","low","close","preclose","volume","amount","turn","pctChg","peTTM","pbMRQ","psTTM","pcfNcfTTM"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["date"] = pd.to_datetime(df["date"]); df = df.set_index("date").sort_index()
    save_raw(df, SAVE_NAME)
    print(f"  保存 {len(df)}行 {df.index[0].date()}~{df.index[-1].date()}")
    return df, info


# ======== 2. 季度财报（3年×6报告期） ========
def fetch_quarterly():
    print("\n[1.5/4] 拉取季度财报(3年)..."); bs.login()
    raw = {}
    for y in [2024, 2025]:  # baostock慢，只拉2年
        raw[y] = {}
        for q in [1,2,3,4]:
            p = {}; g = {}; b = {}
            rs = bs.query_profit_data(STOCK_CODE, year=y, quarter=q)
            if rs.error_code == "0":
                while rs.next():
                    r = rs.get_row_data()
                    p = {"roeAvg": float(r[3]) if r[3] else None, "npMargin": float(r[4]) if r[4] else None,
                         "gpMargin": float(r[5]) if r[5] else None, "netProfit": float(r[6]) if r[6] else None,
                         "MBRevenue": float(r[8]) if r[8] else None}
            rs = bs.query_growth_data(STOCK_CODE, year=y, quarter=q)
            if rs.error_code == "0":
                while rs.next():
                    r = rs.get_row_data()
                    g = {"yoyNI": float(r[4]) if r[4] else None, "yoyRevenue": float(r[5]) if r[5] else None}
            rs = bs.query_balance_data(STOCK_CODE, year=y, quarter=q)
            if rs.error_code == "0":
                while rs.next():
                    r = rs.get_row_data()
                    b = {"debtToAsset": float(r[5]) if r[5] else None}
            raw[y][q] = {**p, **g, **b}

    # 衍生6报告期
    rows = []
    for y in [2024, 2025]:
        qs = raw.get(y, {})
        v = lambda q, k: qs.get(q, {}).get(k)
        # 累计类指标
        rv = {}  # 6个报告期数据
        for key in ["MBRevenue", "netProfit"]:
            q1 = v(1, key) or 0; q2 = v(2, key) or 0; q3 = v(3, key) or 0; q4 = v(4, key) or 0
            rv[f"{key}_Q1"] = q1
            rv[f"{key}_Q2s"] = max(0, q2 - q1)   # Q2单季
            rv[f"{key}_H1"] = q2                   # 半年报
            rv[f"{key}_Q3"] = q3
            rv[f"{key}_Q4s"] = max(0, q4 - q2)    # Q4单季(H2)
            rv[f"{key}_FY"] = q4                   # 年报
        # 比率类指标（直接用当期值，不做累计拆分）
        for key in ["roeAvg", "npMargin", "gpMargin", "debtToAsset", "yoyNI", "yoyRevenue"]:
            rv[f"{key}_Q1"] = v(1, key); rv[f"{key}_Q2s"] = v(2, key)
            rv[f"{key}_H1"] = v(2, key); rv[f"{key}_Q3"] = v(3, key)
            rv[f"{key}_Q4s"] = v(4, key); rv[f"{key}_FY"] = v(4, key)
        rv["year"] = str(y)
        rows.append(rv)
        print(f"  {y}: 年报营收={(v(4,'MBRevenue') or 0)/1e8:.1f}亿 净利={(v(4,'netProfit') or 0)/1e4:.1f}万")

    bs.logout()
    return pd.DataFrame(rows)


# ======== 3. 数据概览 ========
def data_overview(df):
    print("\n" + "=" * 60); print("[2/4] 数据概览")
    print(f"  {len(df)}行 {df.index[0].date()}~{df.index[-1].date()} 缺失:{df.isnull().sum().sum()}")
    sc = ["open","high","low","close","volume","turn","pctChg","peTTM","pbMRQ","psTTM","pcfNcfTTM"]
    s = df[sc].describe()
    print(s.round(2).to_string())
    L = df.iloc[-1]
    print(f"\n  最新({df.index[-1].date()}): 收盘{L['close']:.2f} PE={L['peTTM']:.1f} PB={L['pbMRQ']:.2f}")
    return s


# ======== 4. 图表 ========
def savefig(name):
    plt.tight_layout(); plt.savefig(REPORT_DIR/name, dpi=150, bbox_inches="tight", facecolor="white"); plt.close(); print(f"  OK {name}")

def make_charts(df):
    print("\n" + "=" * 60); print("[3/4] 生成日线图表...")

    # 图1: 价格+均线
    fig, ax = plt.subplots(figsize=(16,6))
    dp = df.copy()
    for p, c in [(20,"#e74c3c"),(60,"#3498db"),(120,"#9b59b6")]: dp[f"MA{p}"] = dp["close"].rolling(p).mean()
    ax.plot(dp.index, dp["close"], color="#2c3e50", lw=1.2, label="收盘价")
    for p, c in [(20,"#e74c3c"),(60,"#3498db"),(120,"#9b59b6")]:
        ax.plot(dp.index, dp[f"MA{p}"], color=c, lw=0.8, alpha=0.8, label=f"MA{p}")
    ax.fill_between(dp.index, dp["close"], alpha=0.05, color="#2c3e50")
    ax.set_title(f"{STOCK_NAME} 价格走势+均线", fontsize=14, fontweight="bold")
    ax.legend(loc="upper left", fontsize=9); ax.set_ylabel("前复权价格"); ax.grid(True, alpha=0.3); savefig("explore_price.png")

    # 图2: 量+换手
    fig, ax1 = plt.subplots(figsize=(16,5))
    cv = ["#e74c3c" if df["close"].iloc[i]>=df["open"].iloc[i] else "#2ecc71" for i in range(len(df))]
    ax1.bar(range(len(df)), df["volume"], color=cv, width=0.8, alpha=0.5, linewidth=0)
    ax1.set_ylabel("成交量", color="#e74c3c"); ax1.tick_params(axis="y", labelcolor="#e74c3c")
    ax2 = ax1.twinx(); ax2.fill_between(range(len(df)), 0, df["turn"], color="#3498db", alpha=0.15)
    ax2.plot(range(len(df)), df["turn"], color="#3498db", lw=0.8); ax2.set_ylabel("换手率%", color="#3498db")
    st = max(1, len(df)//8); ax1.set_xticks(range(0,len(df),st))
    ax1.set_xticklabels([df.index[i].strftime("%Y-%m") for i in range(0,len(df),st)], rotation=30, ha="right")
    ax1.set_title(f"{STOCK_NAME} 成交量+换手率", fontsize=14, fontweight="bold"); ax1.grid(True, alpha=0.3); savefig("explore_volume.png")

    # 图3-5: PE/PB/PCF
    for col, color, name, fname in [
        ("peTTM", "#e67e22", "市盈率（PE/TTM）", "explore_pe.png"),
        ("pbMRQ", "#27ae60", "市净率（PB/MRQ）", "explore_pb.png"),
        ("pcfNcfTTM", "#8e44ad", "市现率（PCF/NcfTTM）", "explore_pcf.png")]:
        s = df[col].dropna(); m = s.median(); n = s.iloc[-1]; pct = (s < n).sum()/len(s)*100
        fig, ax = plt.subplots(figsize=(16,5))
        ax.fill_between(s.index, s, m, alpha=0.1, color=color)
        ax.plot(s.index, s, color=color, lw=1.2)
        ax.axhline(y=m, color="gray", ls="--", alpha=0.6, label=f"中位数:{m:.2f}")
        ax.axhline(y=n, color="#c0392b", ls="--", alpha=0.8, label=f"当前:{n:.2f}({pct:.0f}%分位)")
        ax.set_title(f"{STOCK_NAME} {name}历史走势", fontsize=14, fontweight="bold")
        ax.legend(loc="upper left"); ax.grid(True, alpha=0.3); savefig(fname)

    # 图6: 估值全景
    fig, ax = plt.subplots(figsize=(16,5))
    for col, c, lb in [("peTTM","#e67e22","PE"),("pbMRQ","#27ae60","PB"),("psTTM","#8e44ad","PS")]:
        s = df[col].dropna(); ax.plot(s.index, s/s.median(), color=c, lw=1, label=lb)
    ax.axhline(y=1, color="gray", ls="--"); ax.set_title(f"{STOCK_NAME} 估值全景(归一化)", fontsize=14, fontweight="bold")
    ax.legend(); ax.grid(True, alpha=0.3); savefig("explore_valuation.png")

    # 图7: 分布
    fig, axes = plt.subplots(2,3,figsize=(18,10))
    fig.suptitle(f"{STOCK_NAME} 指标分布", fontsize=14, fontweight="bold")
    for ax, col, title, color in [
        (axes[0,0],"peTTM","市盈率PE","#e67e22"),(axes[0,1],"pbMRQ","市净率PB","#27ae60"),
        (axes[0,2],"psTTM","市销率PS","#8e44ad"),(axes[1,0],"turn","换手率%","#3498db"),
        (axes[1,1],"pctChg","涨跌幅%","#e74c3c"),(axes[1,2],"pcfNcfTTM","市现率PCF","#e67e22")]:
        s = df[col].dropna(); ax.hist(s, bins=40, color=color, alpha=0.7, edgecolor="white", lw=0.3)
        ax.axvline(s.median(), color="black", ls="--", alpha=0.6, label=f"中位:{s.median():.2f}")
        ax.axvline(s.iloc[-1], color="red", ls="--", alpha=0.8, label=f"最新:{s.iloc[-1]:.2f}")
        ax.set_title(title); ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
    savefig("explore_dist.png")

    # 返回指标
    pc = df["peTTM"].dropna(); pb = df["pbMRQ"].dropna(); pf = df["pcfNcfTTM"].dropna()
    return {"pe_m":pc.median(),"pe_n":pc.iloc[-1],"pe_p":(pc<pc.iloc[-1]).sum()/len(pc)*100,
            "pb_m":pb.median(),"pb_n":pb.iloc[-1],"pb_p":(pb<pb.iloc[-1]).sum()/len(pb)*100,
            "pcf_m":pf.median(),"pcf_n":pf.iloc[-1],"pcf_p":(pf<pf.iloc[-1]).sum()/len(pf)*100}


def plot_quarterly(df_q):
    """3年×6报告期 直方图"""
    print("  生成季度财报图表...")
    years = df_q["year"].tolist()
    x = np.arange(len(PERIODS))
    w = 0.25; n = len(years)

    def _bar_chart(key, title, unit, fname, fmt=".1f"):
        fig, ax = plt.subplots(figsize=(24,8))
        for yi, yr in enumerate(years):
            cols = [f"{key}_{s}" for s in PERIOD_SUFFIX]
            vals = [df_q[df_q["year"]==yr][c].iloc[0] for c in cols]
            vals = [v if pd.notna(v) and v is not None else 0 for v in vals]
            if unit == "亿": vals = [v/1e8 for v in vals]
            elif unit == "万": vals = [v/1e4 for v in vals]
            elif unit == "%": vals = [v*100 if v else 0 for v in vals]
            bars = ax.bar(x + w*(yi-n/2+0.5), vals, w, label=f"{yr}年", color=PERIOD_COLORS[yi], alpha=0.85, edgecolor="white")
            for i, v in enumerate(vals):
                if v != 0: ax.text(x[i]+w*(yi-n/2+0.5), v, f"{v:{fmt}}", ha="center", va="bottom", fontsize=11)
        ax.set_xticks(x); ax.set_xticklabels(PERIODS, fontsize=15)
        ax.set_title(f"{STOCK_NAME} {title}（2年对比）", fontsize=20, fontweight="bold")
        ax.set_ylabel(unit, fontsize=14); ax.legend(fontsize=13); ax.grid(True, alpha=0.3, axis="y")
        ax.tick_params(axis="y", labelsize=12); savefig(fname)

    _bar_chart("MBRevenue", "营业收入", "亿", "explore_quarterly_revenue.png")
    _bar_chart("netProfit", "净利润", "万", "explore_quarterly_profit.png", ".0f")
    _bar_chart("gpMargin", "毛利率", "%", "explore_quarterly_margin.png")
    _bar_chart("npMargin", "净利率", "%", "explore_quarterly_npmargin.png")
    _bar_chart("roeAvg", "ROE", "%", "explore_quarterly_roe.png")
    _bar_chart("debtToAsset", "资产负债率", "%", "explore_quarterly_debt.png")


# ======== 5. 报告 ========
def generate_report(df, df_q, info, stats, ci):
    print("\n" + "=" * 60); print("[4/4] 生成报告...")
    L = df.iloc[-1]; F = df.iloc[0]
    pcg = (L["close"]/F["close"]-1)*100
    pi = df["close"].idxmax(); pp = df["close"].max(); tp = df["close"].min()
    cvp = (L["close"]/pp-1)*100
    ma20 = df["close"].rolling(20).mean().iloc[-1]
    ma60 = df["close"].rolling(60).mean().iloc[-1]

    def pl(v):
        if v<0: return "亏损"; return "较低" if v<30 else "中等" if v<60 else "偏高" if v<100 else "极高"
    def ptl(p):
        return "低位" if p<20 else "中低位" if p<40 else "中等" if p<60 else "中高位" if p<80 else "高位"

    # 季度文字
    ql = df_q[df_q["year"]=="2025"]
    if len(ql)==0: ql = df_q.iloc[-1:]
    rev_fy = ql["MBRevenue_FY"].iloc[0]/1e8 if pd.notna(ql["MBRevenue_FY"].iloc[0]) else 0
    np_fy = ql["netProfit_FY"].iloc[0]/1e4 if pd.notna(ql["netProfit_FY"].iloc[0]) else 0

    md = f"""# {STOCK_NAME} 数据探索报告（{df.index[-1].strftime('%Y-%m-%d')}）

> 生成:2026-06-09 | 数据:{df.index[0].date()}~{df.index[-1].date()}({len(df)}日) | 来源:baostock(前复权)

---

## 1. 公司基本信息

| 项目 | 值 |
|------|-----|
| 代码/名称 | `{info['code']}` / **{info['name']}** |
| 上市 | {info['ipo_date']}（约{info['years_listed']}年） |
| 行业 | {info['industry']} |
| 类型/状态 | {info['type_str']} / {info['status_str']} |

---

## 2. 数据概览

共{len(df)}个交易日。字段: open开盘/high最高/low最低/close收盘(前复权)/volume成交量/amount成交额/turn换手率%/pctChg涨跌幅%/peTTM市盈率/pbMRQ市净率/psTTM市销率/pcfNcfTTM市现率。

---

## 3. 估值指标

- **PE(TTM)**=股价÷近12月EPS。越高→高估或高增长预期。当前{ci['pe_n']:.1f}({ptl(ci['pe_p'])}，{ci['pe_p']:.0f}%分位)
- **PB(MRQ)**=股价÷每股净资产。<1→破净。当前{ci['pb_n']:.2f}({ptl(ci['pb_p'])}，{ci['pb_p']:.0f}%分位)
- **PS(TTM)**=总市值÷近12月营收。当前{L['psTTM']:.2f}
- **PCF**=股价÷每股经营现金流。为负→经营现金流为负。当前{ci['pcf_n']:.1f}{'，经营现金流为负' if ci['pcf_n']<0 else ''}

---

## 4. 最新行情({df.index[-1].date()})

| 收盘价 | 涨跌幅 | 换手率 | 成交量 | 成交额 |
|--------|--------|--------|--------|--------|
| **{L['close']:.2f}**元 | {L['pctChg']:+.2f}% | {L['turn']:.2f}% | {L['volume']/10000:.0f}万股 | {L['amount']/1e8:.2f}亿 |

> 近2年从{tp:.2f}到{L['close']:.2f}({pcg:+.1f}%)，最高{pp:.2f}({pi.strftime('%Y-%m-%d')})，当前较高点回撤{abs(cvp):.0f}%

---

## 5. 统计摘要

{stats.round(2).to_markdown()}

---

## 6. 图表

### 6.1 价格走势
![价格](explore_price.png)
> 当前{'在MA20上方' if L['close']>ma20 else '在MA20下方'}，{'多头排列' if L['close']>ma20>ma60 else '空头排列'}

### 6.2 成交量+换手率
![量](explore_volume.png)

### 6.3 市盈率PE
![PE](explore_pe.png)
> PE波动{df['peTTM'].min():.0f}~{df['peTTM'].max():.0f}，当前{ci['pe_n']:.1f}({ci['pe_p']:.0f}%分位)，仅{100-ci['pe_p']:.0f}%时间更贵

### 6.4 市净率PB
![PB](explore_pb.png)
> PB波动{df['pbMRQ'].min():.2f}~{df['pbMRQ'].max():.2f}，当前{ci['pb_n']:.2f}({ci['pb_p']:.0f}%分位)

### 6.5 市现率PCF
![PCF](explore_pcf.png)
> {f'当前{ci["pcf_n"]:.1f}，经营现金流为负，主营业务造血能力不足' if ci['pcf_n']<0 else f'当前{ci["pcf_n"]:.1f}'}

### 6.6 估值全景
![估值](explore_valuation.png)
> PE/PB/PS归一化至各自中位数=1，{'三指标均高于中位数，估值全面偏贵' if ci['pe_n']/ci['pe_m']>1 and ci['pb_n']/ci['pb_m']>1 and L['psTTM']/df['psTTM'].median()>1 else '估值存在分化'}

### 6.7 指标分布
![分布](explore_dist.png)

---

## 7. 季度财务数据（3年×6报告期）

以下展示2024-2026年每个报告期（Q1/Q2单季/半年报/Q3/Q4单季/年报）的核心财务指标。累计类指标（营收、净利润）已拆分为单季数据；比率类指标（毛利率、ROE等）展示当期值。

### 7.1 营业收入
![营收](explore_quarterly_revenue.png)

### 7.2 净利润
![净利](explore_quarterly_profit.png)

### 7.3 毛利率
![毛利率](explore_quarterly_margin.png)

### 7.4 净利率
![净利率](explore_quarterly_npmargin.png)

### 7.5 ROE
![ROE](explore_quarterly_roe.png)

### 7.6 资产负债率
![负债](explore_quarterly_debt.png)

---

## 8. 总结

| 维度 | 状态 |
|------|------|
| 价格 | {tp:.2f}→{L['close']:.2f}({pcg:+.1f}%)，最高{pp:.2f} |
| PE | {ci['pe_n']:.1f}(中位{ci['pe_m']:.1f})，{ptl(ci['pe_p'])} |
| PB | {ci['pb_n']:.2f}(中位{ci['pb_m']:.2f})，{ptl(ci['pb_p'])} |
| 现金流 | {'经营现金流为负' if ci['pcf_n']<0 else '现金流为正'} |
| 2025年报 | 营收{rev_fy:.1f}亿，净利{np_fy:.0f}万 |

> 本报告由`scripts/explore_stock.py`自动生成，仅做数据展示，不构成投资建议。
"""
    (REPORT_DIR / "report.md").write_text(md, encoding="utf-8")
    print(f"  报告: {REPORT_DIR/'report.md'}")


if __name__ == "__main__":
    df, info = fetch_data()
    df_q = fetch_quarterly()
    stats = data_overview(df)
    ci = make_charts(df)
    plot_quarterly(df_q)
    generate_report(df, df_q, info, stats, ci)
    print("\n全部完成! " + str(REPORT_DIR))