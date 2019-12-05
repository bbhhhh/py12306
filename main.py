# -*- coding: utf-8 -*-
import sys

from py12306.app import *
from py12306.helpers.cdn import Cdn
from py12306.log.base import BaseLog
from py12306.log.common_log import CommonLog
from py12306.query.query import Query
from py12306.user.user import User
from py12306.web.web import Web


def main():
    load_argvs()
    CommonLog.print_welcome()
    # 初始化配置
    App.run()
    CommonLog.print_configs()
    # 加载站点信息
    App.did_start()
    #print('App.did_start() done.')
    # 检查运行环境的相关目录以及验证码校验的api用户名密码设置是否正确
    App.run_check()
    #print('App.run_check() done')
    # 初始化查询任务，获取余票查询url
    Query.check_before_run()
    #print('Query.check_before_run() done')

    ####### 运行任务
    Web.run()
    Cdn.run()
    #12306账号登录
    User.run()
    Query.run()
    if not Const.IS_TEST:
        while True:
            sleep(10000)
    else:
        if Config().is_cluster_enabled(): stay_second(5)  # 等待接受完通知
    CommonLog.print_test_complete()


def test():
    """
    功能检查
    包含：
        账号密码验证 (打码)
        座位验证
        乘客验证
        语音验证码验证
        通知验证
    :return:
    """
    Const.IS_TEST = True
    Config.OUT_PUT_LOG_TO_FILE_ENABLED = False
    if '--test-notification' in sys.argv or '-n' in sys.argv:
        Const.IS_TEST_NOTIFICATION = True
    pass


def load_argvs():
    if '--test' in sys.argv or '-t' in sys.argv: test()
    config_index = None

    if '--config' in sys.argv: config_index = sys.argv.index('--config')
    if '-c' in sys.argv: config_index = sys.argv.index('-c')
    if config_index:
        Config.CONFIG_FILE = sys.argv[config_index + 1:config_index + 2].pop()


if __name__ == '__main__':
    main()
