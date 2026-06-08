# -*- coding: utf-8 -*-
"""鑸ぉ鐢靛瓙 鏁版嵁鎺㈢储 鈥?鏃ョ嚎+3骞村搴﹁储鎶?鍥捐〃+鎶ュ憡"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import baostock as bs, pandas as pd, numpy as np
import matplotlib.pyplot as plt, matplotlib.dates as mdates
from data.storage import save_raw

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "Arial"]
plt.rcParams["axes.unicode_minus"] = False

STOCK_CODE = "sz.002851"; STOCK_NAME = "鑸ぉ鐢靛瓙"
START_DATE = "2024-06-09"; END_DATE = "2026-06-09"
REPORT_DIR = Path(__file__).resolve().parent.parent / "research" / f"{STOCK_CODE}-{STOCK_NAME}" / "exploration-20260609b"
SAVE_NAME = "sz_002851"; REPORT_DIR.mkdir(parents=True, exist_ok=True)
FIELDS = "date,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST"
PERIODS = ["Q1","Q2鍗曞","鍗婂勾鎶?,"Q3","Q4鍗曞","骞存姤"]
PERIOD_SUFFIX = ["Q1","Q2s","H1","Q3","Q4s","FY"]  # 瀵瑰簲df_q鍒楀悕鍚庣紑
PERIOD_COLORS = ["#3498db","#2980b9","#2ecc71","#f39c12","#e67e22","#e74c3c"]


# ======== 1. 鏃ョ嚎鏁版嵁 ========
def fetch_data():
    print("=" * 60); print("[1/4] 鎷夊彇鏃ョ嚎..."); bs.login()
    rs = bs.query_stock_basic(STOCK_CODE); info = {}
    while (rs.error_code == "0") & rs.next():
        r = rs.get_row_data()
        info = {"code": r[0], "name": r[1], "ipo_date": r[2], "type": r[4], "status": r[5]}
    rs = bs.query_stock_industry(STOCK_CODE); ind = "鏈煡"
    if rs.error_code == "0":
        while rs.next():
            row = rs.get_row_data()
            ind = row[3] if len(row) > 3 else "鏈煡"
    yl = 2026 - int(info["ipo_date"][:4]) if info["ipo_date"] else 0
    tm = {"1": "鑲＄エ", "2": "鎸囨暟", "3": "鍏朵粬", "4": "ETF", "5": "鍙浆鍊?}
    sm = {"1": "姝ｅ父涓婂競", "0": "宸查€€甯?}
    info.update({"industry": ind, "years_listed": yl, "type_str": tm.get(info.get("type",""),""), "status_str": sm.get(info.get("status",""),"")})
    print(f"  {info['name']}({info['code']}) 涓婂競{info['ipo_date']}({yl}骞? {ind}")

    rs = bs.query_history_k_data_plus(STOCK_CODE, FIELDS, start_date=START_DATE, end_date=END_DATE, frequency="d", adjustflag="2")
    data = []; 
    while (rs.error_code == "0") & rs.next(): data.append(rs.get_row_data())
    bs.logout()
    df = pd.DataFrame(data, columns=rs.fields)
    for c in ["open","high","low","close","preclose","volume","amount","turn","pctChg","peTTM","pbMRQ","psTTM","pcfNcfTTM"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["date"] = pd.to_datetime(df["date"]); df = df.set_index("date").sort_index()
    save_raw(df, SAVE_NAME)
    print(f"  淇濆瓨 {len(df)}琛?{df.index[0].date()}~{df.index[-1].date()}")
    return df, info


# ======== 2. 瀛ｅ害璐㈡姤锛?骞疵?鎶ュ憡鏈燂級 ========
def fetch_quarterly():
    print("\n[1.5/4] 鎷夊彇瀛ｅ害璐㈡姤(3骞?..."); bs.login()
    raw = {}
    for y in [2024, 2025]:  # baostock鎱紝鍙媺2骞?
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

    # 琛嶇敓6鎶ュ憡鏈?
    rows = []
    for y in [2024, 2025]:
        qs = raw.get(y, {})
        v = lambda q, k: qs.get(q, {}).get(k)
        # 绱绫绘寚鏍?
        rv = {}  # 6涓姤鍛婃湡鏁版嵁
        for key in ["MBRevenue", "netProfit"]:
            q1 = v(1, key) or 0; q2 = v(2, key) or 0; q3 = v(3, key) or 0; q4 = v(4, key) or 0
            rv[f"{key}_Q1"] = q1
            rv[f"{key}_Q2s"] = max(0, q2 - q1)   # Q2鍗曞
            rv[f"{key}_H1"] = q2                   # 鍗婂勾鎶?
            rv[f"{key}_Q3"] = q3
            rv[f"{key}_Q4s"] = max(0, q4 - q2)    # Q4鍗曞(H2)
            rv[f"{key}_FY"] = q4                   # 骞存姤
        # 姣旂巼绫绘寚鏍囷紙鐩存帴鐢ㄥ綋鏈熷€硷紝涓嶅仛绱鎷嗗垎锛?
        for key in ["roeAvg", "npMargin", "gpMargin", "debtToAsset", "yoyNI", "yoyRevenue"]:
            rv[f"{key}_Q1"] = v(1, key); rv[f"{key}_Q2s"] = v(2, key)
            rv[f"{key}_H1"] = v(2, key); rv[f"{key}_Q3"] = v(3, key)
            rv[f"{key}_Q4s"] = v(4, key); rv[f"{key}_FY"] = v(4, key)
        rv["year"] = str(y)
        rows.append(rv)
        print(f"  {y}: 骞存姤钀ユ敹={(v(4,'MBRevenue') or 0)/1e8:.1f}浜?鍑€鍒?{(v(4,'netProfit') or 0)/1e4:.1f}涓?)

    bs.logout()
    return pd.DataFrame(rows)


# ======== 3. 鏁版嵁姒傝 ========
def data_overview(df):
    print("\n" + "=" * 60); print("[2/4] 鏁版嵁姒傝")
    print(f"  {len(df)}琛?{df.index[0].date()}~{df.index[-1].date()} 缂哄け:{df.isnull().sum().sum()}")
    sc = ["open","high","low","close","volume","turn","pctChg","peTTM","pbMRQ","psTTM","pcfNcfTTM"]
    s = df[sc].describe()
    print(s.round(2).to_string())
    L = df.iloc[-1]
    print(f"\n  鏈€鏂?{df.index[-1].date()}): 鏀剁洏{L['close']:.2f} PE={L['peTTM']:.1f} PB={L['pbMRQ']:.2f}")
    return s


# ======== 4. 鍥捐〃 ========
def savefig(name):
    plt.tight_layout(); plt.savefig(REPORT_DIR/name, dpi=150, bbox_inches="tight", facecolor="white"); plt.close(); print(f"  OK {name}")

def make_charts(df):
    print("\n" + "=" * 60); print("[3/4] 鐢熸垚鏃ョ嚎鍥捐〃...")

    # 鍥?: 浠锋牸+鍧囩嚎
    fig, ax = plt.subplots(figsize=(16,6))
    dp = df.copy()
    for p, c in [(20,"#e74c3c"),(60,"#3498db"),(120,"#9b59b6")]: dp[f"MA{p}"] = dp["close"].rolling(p).mean()
    ax.plot(dp.index, dp["close"], color="#2c3e50", lw=1.2, label="鏀剁洏浠?)
    for p, c in [(20,"#e74c3c"),(60,"#3498db"),(120,"#9b59b6")]:
        ax.plot(dp.index, dp[f"MA{p}"], color=c, lw=0.8, alpha=0.8, label=f"MA{p}")
    ax.fill_between(dp.index, dp["close"], alpha=0.05, color="#2c3e50")
    ax.set_title(f"{STOCK_NAME} 浠锋牸璧板娍+鍧囩嚎", fontsize=14, fontweight="bold")
    ax.legend(loc="upper left", fontsize=9); ax.set_ylabel("鍓嶅鏉冧环鏍?); ax.grid(True, alpha=0.3); savefig("explore_price.png")

    # 鍥?: 閲?鎹㈡墜
    fig, ax1 = plt.subplots(figsize=(16,5))
    cv = ["#e74c3c" if df["close"].iloc[i]>=df["open"].iloc[i] else "#2ecc71" for i in range(len(df))]
    ax1.bar(range(len(df)), df["volume"], color=cv, width=0.8, alpha=0.5, linewidth=0)
    ax1.set_ylabel("鎴愪氦閲?, color="#e74c3c"); ax1.tick_params(axis="y", labelcolor="#e74c3c")
    ax2 = ax1.twinx(); ax2.fill_between(range(len(df)), 0, df["turn"], color="#3498db", alpha=0.15)
    ax2.plot(range(len(df)), df["turn"], color="#3498db", lw=0.8); ax2.set_ylabel("鎹㈡墜鐜?", color="#3498db")
    st = max(1, len(df)//8); ax1.set_xticks(range(0,len(df),st))
    ax1.set_xticklabels([df.index[i].strftime("%Y-%m") for i in range(0,len(df),st)], rotation=30, ha="right")
    ax1.set_title(f"{STOCK_NAME} 鎴愪氦閲?鎹㈡墜鐜?, fontsize=14, fontweight="bold"); ax1.grid(True, alpha=0.3); savefig("explore_volume.png")

    # 鍥?-5: PE/PB/PCF
    for col, color, name, fname in [
        ("peTTM", "#e67e22", "甯傜泩鐜囷紙PE/TTM锛?, "explore_pe.png"),
        ("pbMRQ", "#27ae60", "甯傚噣鐜囷紙PB/MRQ锛?, "explore_pb.png"),
        ("pcfNcfTTM", "#8e44ad", "甯傜幇鐜囷紙PCF/NcfTTM锛?, "explore_pcf.png")]:
        s = df[col].dropna(); m = s.median(); n = s.iloc[-1]; pct = (s < n).sum()/len(s)*100
        fig, ax = plt.subplots(figsize=(16,5))
        ax.fill_between(s.index, s, m, alpha=0.1, color=color)
        ax.plot(s.index, s, color=color, lw=1.2)
        ax.axhline(y=m, color="gray", ls="--", alpha=0.6, label=f"涓綅鏁?{m:.2f}")
        ax.axhline(y=n, color="#c0392b", ls="--", alpha=0.8, label=f"褰撳墠:{n:.2f}({pct:.0f}%鍒嗕綅)")
        ax.set_title(f"{STOCK_NAME} {name}鍘嗗彶璧板娍", fontsize=14, fontweight="bold")
        ax.legend(loc="upper left"); ax.grid(True, alpha=0.3); savefig(fname)

    # 鍥?: 浼板€煎叏鏅?
    fig, ax = plt.subplots(figsize=(16,5))
    for col, c, lb in [("peTTM","#e67e22","PE"),("pbMRQ","#27ae60","PB"),("psTTM","#8e44ad","PS")]:
        s = df[col].dropna(); ax.plot(s.index, s/s.median(), color=c, lw=1, label=lb)
    ax.axhline(y=1, color="gray", ls="--"); ax.set_title(f"{STOCK_NAME} 浼板€煎叏鏅?褰掍竴鍖?", fontsize=14, fontweight="bold")
    ax.legend(); ax.grid(True, alpha=0.3); savefig("explore_valuation.png")

    # 鍥?: 鍒嗗竷
    fig, axes = plt.subplots(2,3,figsize=(18,10))
    fig.suptitle(f"{STOCK_NAME} 鎸囨爣鍒嗗竷", fontsize=14, fontweight="bold")
    for ax, col, title, color in [
        (axes[0,0],"peTTM","甯傜泩鐜嘝E","#e67e22"),(axes[0,1],"pbMRQ","甯傚噣鐜嘝B","#27ae60"),
        (axes[0,2],"psTTM","甯傞攢鐜嘝S","#8e44ad"),(axes[1,0],"turn","鎹㈡墜鐜?","#3498db"),
        (axes[1,1],"pctChg","娑ㄨ穼骞?","#e74c3c"),(axes[1,2],"pcfNcfTTM","甯傜幇鐜嘝CF","#e67e22")]:
        s = df[col].dropna(); ax.hist(s, bins=40, color=color, alpha=0.7, edgecolor="white", lw=0.3)
        ax.axvline(s.median(), color="black", ls="--", alpha=0.6, label=f"涓綅:{s.median():.2f}")
        ax.axvline(s.iloc[-1], color="red", ls="--", alpha=0.8, label=f"鏈€鏂?{s.iloc[-1]:.2f}")
        ax.set_title(title); ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
    savefig("explore_dist.png")

    # 杩斿洖鎸囨爣
    pc = df["peTTM"].dropna(); pb = df["pbMRQ"].dropna(); pf = df["pcfNcfTTM"].dropna()
    return {"pe_m":pc.median(),"pe_n":pc.iloc[-1],"pe_p":(pc<pc.iloc[-1]).sum()/len(pc)*100,
            "pb_m":pb.median(),"pb_n":pb.iloc[-1],"pb_p":(pb<pb.iloc[-1]).sum()/len(pb)*100,
            "pcf_m":pf.median(),"pcf_n":pf.iloc[-1],"pcf_p":(pf<pf.iloc[-1]).sum()/len(pf)*100}


def plot_quarterly(df_q):
    """3骞疵?鎶ュ憡鏈?鐩存柟鍥?""
    print("  鐢熸垚瀛ｅ害璐㈡姤鍥捐〃...")
    years = df_q["year"].tolist()
    x = np.arange(len(PERIODS))
    w = 0.25; n = len(years)

    def _bar_chart(key, title, unit, fname, fmt=".1f"):
        fig, ax = plt.subplots(figsize=(24,8))
        for yi, yr in enumerate(years):
            cols = [f"{key}_{s}" for s in PERIOD_SUFFIX]
            vals = [df_q[df_q["year"]==yr][c].iloc[0] for c in cols]
            vals = [v if pd.notna(v) and v is not None else 0 for v in vals]
            if unit == "浜?: vals = [v/1e8 for v in vals]
            elif unit == "涓?: vals = [v/1e4 for v in vals]
            elif unit == "%": vals = [v*100 if v else 0 for v in vals]
            bars = ax.bar(x + w*(yi-n/2+0.5), vals, w, label=f"{yr}骞?, color=PERIOD_COLORS[yi], alpha=0.85, edgecolor="white")
            for i, v in enumerate(vals):
                if v != 0: ax.text(x[i]+w*(yi-n/2+0.5), v, f"{v:{fmt}}", ha="center", va="bottom", fontsize=11)
        ax.set_xticks(x); ax.set_xticklabels(PERIODS, fontsize=15)
        ax.set_title(f"{STOCK_NAME} {title}锛?骞村姣旓級", fontsize=20, fontweight="bold")
        ax.set_ylabel(unit, fontsize=14); ax.legend(fontsize=13); ax.grid(True, alpha=0.3, axis="y")
        ax.tick_params(axis="y", labelsize=12); savefig(fname)

    _bar_chart("MBRevenue", "钀ヤ笟鏀跺叆", "浜?, "explore_quarterly_revenue.png")
    _bar_chart("netProfit", "鍑€鍒╂鼎", "涓?, "explore_quarterly_profit.png", ".0f")
    _bar_chart("gpMargin", "姣涘埄鐜?, "%", "explore_quarterly_margin.png")
    _bar_chart("npMargin", "鍑€鍒╃巼", "%", "explore_quarterly_npmargin.png")
    _bar_chart("roeAvg", "ROE", "%", "explore_quarterly_roe.png")
    _bar_chart("debtToAsset", "璧勪骇璐熷€虹巼", "%", "explore_quarterly_debt.png")


# ======== 5. 鎶ュ憡 ========
def generate_report(df, df_q, info, stats, ci):
    print("\n" + "=" * 60); print("[4/4] 鐢熸垚鎶ュ憡...")
    L = df.iloc[-1]; F = df.iloc[0]
    pcg = (L["close"]/F["close"]-1)*100
    pi = df["close"].idxmax(); pp = df["close"].max(); tp = df["close"].min()
    cvp = (L["close"]/pp-1)*100
    ma20 = df["close"].rolling(20).mean().iloc[-1]
    ma60 = df["close"].rolling(60).mean().iloc[-1]

    def pl(v):
        if v<0: return "浜忔崯"; return "杈冧綆" if v<30 else "涓瓑" if v<60 else "鍋忛珮" if v<100 else "鏋侀珮"
    def ptl(p):
        return "浣庝綅" if p<20 else "涓綆浣? if p<40 else "涓瓑" if p<60 else "涓珮浣? if p<80 else "楂樹綅"

    # 瀛ｅ害鏂囧瓧
    ql = df_q[df_q["year"]=="2025"]
    if len(ql)==0: ql = df_q.iloc[-1:]
    rev_fy = ql["MBRevenue_FY"].iloc[0]/1e8 if pd.notna(ql["MBRevenue_FY"].iloc[0]) else 0
    np_fy = ql["netProfit_FY"].iloc[0]/1e4 if pd.notna(ql["netProfit_FY"].iloc[0]) else 0

    md = f"""# {STOCK_NAME} 鏁版嵁鎺㈢储鎶ュ憡锛坽df.index[-1].strftime('%Y-%m-%d')}锛?

> 鐢熸垚:2026-06-09 | 鏁版嵁:{df.index[0].date()}~{df.index[-1].date()}({len(df)}鏃? | 鏉ユ簮:baostock(鍓嶅鏉?

---

## 1. 鍏徃鍩烘湰淇℃伅

| 椤圭洰 | 鍊?|
|------|-----|
| 浠ｇ爜/鍚嶇О | `{info['code']}` / **{info['name']}** |
| 涓婂競 | {info['ipo_date']}锛堢害{info['years_listed']}骞达級 |
| 琛屼笟 | {info['industry']} |
| 绫诲瀷/鐘舵€?| {info['type_str']} / {info['status_str']} |

---

## 2. 鏁版嵁姒傝

鍏眥len(df)}涓氦鏄撴棩銆傚瓧娈? open寮€鐩?high鏈€楂?low鏈€浣?close鏀剁洏(鍓嶅鏉?/volume鎴愪氦閲?amount鎴愪氦棰?turn鎹㈡墜鐜?/pctChg娑ㄨ穼骞?/peTTM甯傜泩鐜?pbMRQ甯傚噣鐜?psTTM甯傞攢鐜?pcfNcfTTM甯傜幇鐜囥€?

---

## 3. 浼板€兼寚鏍?

- **PE(TTM)**=鑲′环梅杩?2鏈圗PS銆傝秺楂樷啋楂樹及鎴栭珮澧為暱棰勬湡銆傚綋鍓峽ci['pe_n']:.1f}({ptl(ci['pe_p'])}锛寋ci['pe_p']:.0f}%鍒嗕綅)
- **PB(MRQ)**=鑲′环梅姣忚偂鍑€璧勪骇銆?1鈫掔牬鍑€銆傚綋鍓峽ci['pb_n']:.2f}({ptl(ci['pb_p'])}锛寋ci['pb_p']:.0f}%鍒嗕綅)
- **PS(TTM)**=鎬诲競鍊济疯繎12鏈堣惀鏀躲€傚綋鍓峽L['psTTM']:.2f}
- **PCF**=鑲′环梅姣忚偂缁忚惀鐜伴噾娴併€備负璐熲啋缁忚惀鐜伴噾娴佷负璐熴€傚綋鍓峽ci['pcf_n']:.1f}{'锛岀粡钀ョ幇閲戞祦涓鸿礋' if ci['pcf_n']<0 else ''}

---

## 4. 鏈€鏂拌鎯?{df.index[-1].date()})

| 鏀剁洏浠?| 娑ㄨ穼骞?| 鎹㈡墜鐜?| 鎴愪氦閲?| 鎴愪氦棰?|
|--------|--------|--------|--------|--------|
| **{L['close']:.2f}**鍏?| {L['pctChg']:+.2f}% | {L['turn']:.2f}% | {L['volume']/10000:.0f}涓囪偂 | {L['amount']/1e8:.2f}浜?|

> 杩?骞翠粠{tp:.2f}鍒皗L['close']:.2f}({pcg:+.1f}%)锛屾渶楂榹pp:.2f}({pi.strftime('%Y-%m-%d')})锛屽綋鍓嶈緝楂樼偣鍥炴挙{abs(cvp):.0f}%

---

## 5. 缁熻鎽樿

{stats.round(2).to_markdown()}

---

## 6. 鍥捐〃

### 6.1 浠锋牸璧板娍
![浠锋牸](explore_price.png)
> 褰撳墠{'鍦∕A20涓婃柟' if L['close']>ma20 else '鍦∕A20涓嬫柟'}锛寋'澶氬ご鎺掑垪' if L['close']>ma20>ma60 else '绌哄ご鎺掑垪'}

### 6.2 鎴愪氦閲?鎹㈡墜鐜?
![閲廬(explore_volume.png)

### 6.3 甯傜泩鐜嘝E
![PE](explore_pe.png)
> PE娉㈠姩{df['peTTM'].min():.0f}~{df['peTTM'].max():.0f}锛屽綋鍓峽ci['pe_n']:.1f}({ci['pe_p']:.0f}%鍒嗕綅)锛屼粎{100-ci['pe_p']:.0f}%鏃堕棿鏇磋吹

### 6.4 甯傚噣鐜嘝B
![PB](explore_pb.png)
> PB娉㈠姩{df['pbMRQ'].min():.2f}~{df['pbMRQ'].max():.2f}锛屽綋鍓峽ci['pb_n']:.2f}({ci['pb_p']:.0f}%鍒嗕綅)

### 6.5 甯傜幇鐜嘝CF
![PCF](explore_pcf.png)
> {f'褰撳墠{ci["pcf_n"]:.1f}锛岀粡钀ョ幇閲戞祦涓鸿礋锛屼富钀ヤ笟鍔￠€犺鑳藉姏涓嶈冻' if ci['pcf_n']<0 else f'褰撳墠{ci["pcf_n"]:.1f}'}

### 6.6 浼板€煎叏鏅?
![浼板€糫(explore_valuation.png)
> PE/PB/PS褰掍竴鍖栬嚦鍚勮嚜涓綅鏁?1锛寋'涓夋寚鏍囧潎楂樹簬涓綅鏁帮紝浼板€煎叏闈㈠亸璐? if ci['pe_n']/ci['pe_m']>1 and ci['pb_n']/ci['pb_m']>1 and L['psTTM']/df['psTTM'].median()>1 else '浼板€煎瓨鍦ㄥ垎鍖?}

### 6.7 鎸囨爣鍒嗗竷
![鍒嗗竷](explore_dist.png)

---

## 7. 瀛ｅ害璐㈠姟鏁版嵁锛?骞疵?鎶ュ憡鏈燂級

浠ヤ笅灞曠ず2024-2026骞存瘡涓姤鍛婃湡锛圦1/Q2鍗曞/鍗婂勾鎶?Q3/Q4鍗曞/骞存姤锛夌殑鏍稿績璐㈠姟鎸囨爣銆傜疮璁＄被鎸囨爣锛堣惀鏀躲€佸噣鍒╂鼎锛夊凡鎷嗗垎涓哄崟瀛ｆ暟鎹紱姣旂巼绫绘寚鏍囷紙姣涘埄鐜囥€丷OE绛夛級灞曠ず褰撴湡鍊笺€?

### 7.1 钀ヤ笟鏀跺叆
![钀ユ敹](explore_quarterly_revenue.png)

### 7.2 鍑€鍒╂鼎
![鍑€鍒(explore_quarterly_profit.png)

### 7.3 姣涘埄鐜?
![姣涘埄鐜嘳(explore_quarterly_margin.png)

### 7.4 鍑€鍒╃巼
![鍑€鍒╃巼](explore_quarterly_npmargin.png)

### 7.5 ROE
![ROE](explore_quarterly_roe.png)

### 7.6 璧勪骇璐熷€虹巼
![璐熷€篯(explore_quarterly_debt.png)

---

## 8. 鎬荤粨

| 缁村害 | 鐘舵€?|
|------|------|
| 浠锋牸 | {tp:.2f}鈫抺L['close']:.2f}({pcg:+.1f}%)锛屾渶楂榹pp:.2f} |
| PE | {ci['pe_n']:.1f}(涓綅{ci['pe_m']:.1f})锛寋ptl(ci['pe_p'])} |
| PB | {ci['pb_n']:.2f}(涓綅{ci['pb_m']:.2f})锛寋ptl(ci['pb_p'])} |
| 鐜伴噾娴?| {'缁忚惀鐜伴噾娴佷负璐? if ci['pcf_n']<0 else '鐜伴噾娴佷负姝?} |
| 2025骞存姤 | 钀ユ敹{rev_fy:.1f}浜匡紝鍑€鍒﹞np_fy:.0f}涓?|

> 鏈姤鍛婄敱`scripts/explore_stock.py`鑷姩鐢熸垚锛屼粎鍋氭暟鎹睍绀猴紝涓嶆瀯鎴愭姇璧勫缓璁€?
"""
    (REPORT_DIR / "report.md").write_text(md, encoding="utf-8")
    print(f"  鎶ュ憡: {REPORT_DIR/'report.md'}")


if __name__ == "__main__":
    df, info = fetch_data()
    df_q = fetch_quarterly()
    stats = data_overview(df)
    ci = make_charts(df)
    plot_quarterly(df_q)
    generate_report(df, df_q, info, stats, ci)
    print("\n鍏ㄩ儴瀹屾垚! " + str(REPORT_DIR))
