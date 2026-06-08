"""选股模块
条件筛选、多因子排序、行业筛选等。
"""


def filter_by_condition(df, conditions: dict):
    """按条件筛选股票

    Args:
        df: 股票数据
        conditions: 筛选条件，如 {'pe': ('<', 20), 'roe': ('>', 0.15)}

    Returns:
        筛选后的 DataFrame
    """
    # TODO
    pass


def rank_by_factors(df, factors: list):
    """多因子打分排序"""
    # TODO
    pass
