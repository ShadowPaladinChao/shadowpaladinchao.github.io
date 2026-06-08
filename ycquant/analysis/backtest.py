"""简易回测
单标的 / 多标的历史回测，输出收益曲线、回撤曲线、绩效指标。
"""


def run_backtest(strategy, data, **kwargs):
    """运行回测

    Args:
        strategy: 策略对象
        data: 行情数据

    Returns:
        dict: {'returns': Series, 'metrics': dict}
    """
    # TODO
    pass


def calc_metrics(returns):
    """计算绩效指标：年化收益、夏普比率、最大回撤等"""
    # TODO
    pass
