# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
import time
from LoginPage import LoginPage
from BaseTaskPage import BaseTaskPage
from TestCaseInfo import TestCaseInfo
from TestReport import TestReport
from Commons import Commons


class TestShopTaskCreate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.10.141.79:8080/icompaign/login.html"
        self.driver.maximize_window()
        self.testcaseinfo = TestCaseInfo(caseid="2", name="create shop task", owner="liuyang")
        self.testresult = TestReport()

    def test_ShopTaskCreate(self):
        try:
            self.testcaseinfo.starttime = str(time.strftime("%Y-%m-%d %H:%M:%S"))
            self.driver.get(self.base_url)
            time.sleep(1)
            loginpage = LoginPage(self.driver)
            loginpage.login_icompaign("19444444444", "1")
            time.sleep(1)
            taskpage = BaseTaskPage(self.driver)
            taskpage.menu_click()
            taskpage.task_create_click()
            self.assertEqual(taskpage.get_stepname(1), u"任务基本信息", "step1 error")
            taskname = taskpage.set_tname(u"Auto_炒店任务_")
            # 类型选择：新发展客户，流量提升，语音提升，短信提升，国际业务，增值推荐 ······
            taskpage.set_tbusiness(u"语音提升")
            taskpage.set_tbtime(time.strftime("%Y-%m-%d"))
            taskpage.set_tstime(time.strftime("%Y-%m-%d"))
            taskpage.set_shop()
            taskpage.set_tdesc(u"This is a testing task")
            taskpage.next1_click()
            time.sleep(1)
            self.assertEqual(taskpage.get_stepname(2), u"目标用户选择", "step1 is not change to step2")
            taskpage.next1_click()
            self.assertEqual(taskpage.get_stepname(3), u"客户接触渠道", "step2 is not change to step3")
            taskpage.set_sms(u"安讯科技智能营销测试短信！")
            taskpage.set_interval(1)
            taskpage.next1_click()
            self.assertEqual(taskpage.get_stepname(4), u"预览", "step3 is not change to step4")
            taskpage.commit_click()
            # 需要优化等待方式
            time.sleep(20)
            print taskpage.get_rowname()
            print taskname
            self.assertEqual(taskpage.get_rowname(), taskname, "task created faild! or other task created on row1")
            self.testcaseinfo.result = "pass"
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
