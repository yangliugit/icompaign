# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
from TestCaseInfo import TestCaseInfo
from LoginPage import LoginPage
from ShopTaskPoolPage import ShopTaskPoolPage
from TestReport import TestReport
from Commons import Commons


class TestTaskPool(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.10.141.79:8080/icompaign/login.html"
        self.driver.maximize_window()
        self.testcaseinfo = TestCaseInfo(caseid="4", name="execute shop task", owner="liuyang")
        self.testresult = TestReport()

    def test_ShopTaskPool(self):
        try:
            self.testcaseinfo.starttime = str(time.strftime("%Y-%m-%d %H:%M:%S"))
            self.driver.get(self.base_url)
            time.sleep(1)
            loginpage = LoginPage(self.driver)
            loginpage.login_icompaign("19444444444", "1")
            time.sleep(1)
            shoptaskpoolpage = ShopTaskPoolPage(self.driver)
            shoptaskpoolpage.pool_menu_click()
            time.sleep(1)
            firsttaskname = shoptaskpoolpage.get_first_task_name()
            if firsttaskname.startswith(u"Auto"):
                shoptaskpoolpage.execute_task()
                boxtaskname = shoptaskpoolpage.get_box_taskname()
                self.assertEqual(boxtaskname, firsttaskname, "execute shop taskname is not equal!")
                shoptaskpoolpage.execute_confirm()
                time.sleep(1)
                state = shoptaskpoolpage.get_state()
                print state
                self.testcaseinfo.result = "pass"
            else:
                self.testcaseinfo.errorinfo = "the first task isn't autotask! please check"
                self.testcaseinfo.result = "faild"

        except Exception as err:
            c = Commons(self.driver)
            c.exception_picture(self._testMethodName)
            self.testcaseinfo.errorinfo = str(err)
        finally:
            self.testcaseinfo.endtime = str(time.strftime("%Y-%m-%d %H:%M:%S"))
            print self.testcaseinfo.caseid, self.testcaseinfo.starttime, self.testcaseinfo.endtime, \
                self.testcaseinfo.name, self.testcaseinfo.result, self.testcaseinfo.errorinfo

    def tearDown(self):
        self.driver.close()
        # testresult write in report
        self.testresult.write_html(self.testcaseinfo)

if __name__ == '__main__':
    unittest.main()
