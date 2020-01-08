# -*- coding: utf-8 -*-
class BasePage(object):

    # 销毁创建的测试数据方法可以放在此处
    def __init__(self, driver):
        self.driver = driver
