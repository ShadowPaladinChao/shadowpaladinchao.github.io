"""数据获取模块
基于 akshare 等数据源获取行情、财务数据。
"""


def get_daily(stock_code: str, start_date: str = None, end_date: str = None):
    """获取个股日线数据

    Args:
        stock_code: 股票代码，如 '000001'
        start_date: 开始日期 'YYYY-MM-DD'
        end_date: 结束日期 'YYYY-MM-DD'

    Returns:
        DataFrame
    """
    # TODO
    pass


def get_index_daily(index_code: str, start_date: str = None, end_date: str = None):
    """获取指数日线数据"""
    # TODO
    pass


def get_financial(stock_code: str, report_type: str = "年报"):
    """获取财务数据"""
    # TODO
    pass
