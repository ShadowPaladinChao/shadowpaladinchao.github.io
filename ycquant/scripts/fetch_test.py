"""数据拉取测试
使用 baostock 拉取 A 股日线数据，存入 data/raw/stock/

注：akshare 被公司防火墙拦截，改用 baostock（TCP 协议不受 HTTP 代理影响）。
    如网络环境允许 akshare，将 setup_network() 取消注释并切换 fetch 函数即可。
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# from config.network import setup_network
# setup_network()  # 绕过系统代理（akshare 专用）

import baostock as bs
import pandas as pd
from data.storage import save_raw, load_raw, list_raw, has_raw

# ============ 配置 ============
# baostock 代码格式: sh.600519 (上交所), sz.000001 (深交所)
STOCKS = {
    "sh.600519": "贵州茅台",
    "sz.000001": "平安银行",
    "sz.000002": "万科A",
}
START_DATE = "2023-01-01"
END_DATE = "2025-06-08"


def fetch_one_bs(stock_code: str) -> pd.DataFrame:
    """从 baostock 获取个股日线（前复权）"""
    rs = bs.query_history_k_data_plus(
        stock_code,
        "date,open,high,low,close,volume,amount,pctChg,turn",
        start_date=START_DATE,
        end_date=END_DATE,
        frequency="d",
        adjustflag="2",  # 前复权
    )
    data_list = []
    while (rs.error_code == "0") & rs.next():
        data_list.append(rs.get_row_data())

    if not data_list:
        raise ValueError(f"baostock 未返回数据: {stock_code}")

    df = pd.DataFrame(data_list, columns=rs.fields)
    df["date"] = pd.to_datetime(df["date"])
    for col in ["open", "high", "low", "close", "volume", "amount", "pctChg", "turn"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.set_index("date").sort_index()
    return df


def main():
    bs.login()
    print("=" * 50)
    print("ycquant 数据拉取测试 (baostock)")
    print("=" * 50)

    for code, name in STOCKS.items():
        fname = code.replace(".", "_")  # sh.600519 → sh_600519
        print(f"\n>>> 处理: {code} ({name})")
        if has_raw(fname):
            df = load_raw(fname)
            print(f"    已缓存，读取本地: {len(df)} 条记录")
        else:
            try:
                df = fetch_one_bs(code)
                save_raw(df, fname)
                print(f"    拉取成功: {len(df)} 条记录, {df.index[0].date()} ~ {df.index[-1].date()}")
            except Exception as e:
                print(f"    拉取失败: {e}")
                continue

        print(df.head(3).to_string())

    bs.logout()

    print(f"\n{'=' * 50}")
    print(f"已缓存股票: {list_raw()}")


if __name__ == "__main__":
    main()
