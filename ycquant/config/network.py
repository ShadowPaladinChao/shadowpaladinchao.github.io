"""网络配置 - 绕过系统代理
在 import akshare 之前调用 setup_network() 即可。
"""
import requests


def setup_network():
    """配置网络：禁用系统代理（适用于公司内网环境）

    akshare 内部使用 requests.Session，默认会读取 Windows 系统代理。
    通过猴子补丁强制 Session.trust_env = False，绕过系统代理。
    """
    OriginalSession = requests.Session

    class NoProxySession(OriginalSession):
        def __init__(self):
            super().__init__()
            self.trust_env = False  # 关键：不从系统读取代理设置

    requests.Session = NoProxySession

    # requests.get / post 内部是 `with sessions.Session() as session: session.get(...)`
    # 由于我们已替换 Session 类，它们会自动使用 NoProxySession
