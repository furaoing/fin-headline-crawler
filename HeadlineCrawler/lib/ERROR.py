# -*- coding: utf-8 -*-


class GeneralError(BaseException):
    """
    GenarateException
    """
    code = 5
    spec = 'GeneralError'
    desc = u'程序内部其他普通错误'

    def __str__(self):
        return '{}:{} {}'.format(self.spec, self.code, self.desc)


class MatchError(GeneralError):
    code = 1006
    spec = 'Match Error'
    desc = u'正则或者 XPATH 解析错误'


class TimeoutError(GeneralError):
    code = 11
    spec = 'Timeout Error'
    desc = u'网页连接超时'


class MysqlError(GeneralError):
    code = 1004
    spec = 'Mysql Error'
    desc = u'Mysql 交互错误'


class ESError(GeneralError):
    code = 1005
    spec = 'ES Error'
    desc = 'ES 交互错误'


class GeneralConnectError(GeneralError):
    """
    GeneralConnectError
    """
    code = 10
    spec = 'GeneralConnectError'
    desc = u'一般连接错误'


class DNSProblem(GeneralConnectError):
    code = 12
    spec = 'DNSProblem'
    desc = u'DNS出错'


class Http404Error(GeneralConnectError):
    code = 14
    spec = '404 Error'
    desc = u'404错误'


class Http50XError(GeneralConnectError):
    code = 15
    spec = '50X Error'
    desc = u'50X错误'