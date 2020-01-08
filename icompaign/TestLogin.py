# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
from TestCaseInfo import TestCaseInfo
from LoginPage import LoginPage
from TestReport import TestReport
from Commons import Commons


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.10.141.79:8080/icompaign/login.html"
        self.driver.maximize_window()
        # testcase information
        self.testcaseinfo = TestCaseInfo(caseid="1", name="login to icompaign system", owner="liuyang")
        # declear testreport
        self.testresult = TestReport()

    def test_Login(self):
        try:
            self.testcaseinfo.starttime = str(time.strftime("%Y-%m-%d %H:%M:%S"))
            # step 1
            self.driver.get(self.base_url)
            # step 2
            login_page = LoginPage(self.driver)
            # step 3
            login_page.click_change()
            # step 4
            login_page.set_username("12345678987")
            # step 5
            login_page.set_password("qwe123")
            # input verifcode
            login_page.set_verif("yyhh")
            # check point1: check icompaign title
            self.assertEqual(login_page.get_title(), u"江苏联通智能营销平台", "before page title is not equal")
            # login
            login_page.click_sign()
            self.assertEqual(login_page.get_title(), u"江苏联通智能营销平台", "after page title is not equal")
            # right test resule
            self.testcaseinfo.result = "Pass"
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

if __name__ == "__main__":
    unittest.main()
