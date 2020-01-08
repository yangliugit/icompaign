# --*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
from LoginPage import LoginPage
from ShopTaskAduitPage import ShopTaskAuditPage
from TestCaseInfo import TestCaseInfo
from BaseTaskPage import BaseTaskPage
from TestReport import TestReport
from Commons import Commons
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class TestShopTaskAudit(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.10.141.79:8080/icompaign/login.html"
        self.driver.maximize_window()
        self.testcaseinfo = TestCaseInfo(caseid="3", name="audit shop task", owner="liuyang")
        self.testresult = TestReport()

    def test_ShopTaskAudit(self):
        try:
            self.testcaseinfo.starttime = str(time.strftime("%Y-%m-%d %H:%M:%S"))
            self.driver.get(self.base_url)
            time.sleep(1)
            loginpage = LoginPage(self.driver)
            loginpage.login_icompaign("19333333333", "1")
            time.sleep(1)
            auditpage = ShopTaskAuditPage(self.driver)
            auditpage.menu_click()
            firsttaskname = auditpage.get_first_task_name()
            # firsttaskname = firsttaskname.encode("utf-8")
            if firsttaskname.startswith(u"Auto"):
                auditpage.audit_click()
                auditpage.audit("pass", "test pass")
                time.sleep(20)
                shoptaskpage = BaseTaskPage(self.driver)
                shoptaskpage.menu_click()
                t_state = shoptaskpage.get_task_state(firsttaskname)
                print t_state
                self.assertEqual(t_state, u"审核成功", "task state is wrong")
                self.testcaseinfo.result = "pass"
            else:
                print "the first task isn't autotask! please check"
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

if __name__ == "__main__":
    unittest.main()
