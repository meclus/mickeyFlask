class dbconnect(object):
    """db connect config class"""

    def __init__(self, host, port, username, password, database):
        super(dbconnect, self).__init__()
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database


class serverconf(object):
    """server config class"""

    def __init__(self, host, serviceport, webport, domain, account, password):
        super(serverconf, self).__init__()
        self.domain = domain
        self.host = host
        self.webport = webport
        self.serviceport = serviceport
        self.account = account
        self.password = password

    def __str__(self):
        return str(dict((name, getattr(self, name)) for name in dir(self) if not name.startswith('__')))

    def getconf(self, param='test'):
        if param == 'test':
            return serverconf("192.168.104.201", "8000", "7007", "platform-test.mobilemd.cn", "meclus", "123456")
        elif param == 'uat':
            return serverconf("10.3.0.3", "8012", "8010", "grayscale-platform.mobilemd.cn", "meclus", "8665Meclus")
        elif param == 'event':
            return serverconf("10.3.0.5", "7000", "8010", "event-platform.mobilemd.cn", "yafei.hu@mobilemd.cn", "Aaa123")
        elif param == 'demo':
            return serverconf("10.64.0.6", "8011", "8010", "demo-platform.mobilemd.cn", "yafei.hu@mobilemd.cn", "Hyf19961213")
        elif param == 'prod':
            return serverconf("10.1.64.21", "7000", "8011", "platform.mobilemd.cn", "meng.wang@mobilemd.cn", "111111")

    def getsystem(self):
        import platform
        return platform.system()