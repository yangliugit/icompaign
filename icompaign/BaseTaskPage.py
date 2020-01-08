# -*- coding:utf-8 -*-
from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class BaseTaskPage(BasePage):
    m_tcenter = (By.ID, "60")
    m_tshop = (By.ID, "70")
    m_tshop_create = (By.ID, "73")
    btn_tshop_create = (By.ID, "createShopTaskButton")
    t_name = (By.CLASS_NAME, "taskName")
    t_business = (By.CLASS_NAME, "businessId")
    t_btime = (By.CLASS_NAME, "startTime")
    t_stime = (By.CLASS_NAME, "stopTime")
    t_shop = (By.CLASS_NAME, "baseName")
    btn_shop_choose = (By.ID, "btnRightAll")
    btn_confirm = (By.CLASS_NAME, "layui-layer-btn0")
    t_desc = (By.CLASS_NAME, "taskDesc")
    btn_next1 = (By.XPATH, "//*[@id='createShopTaskDialog']/div/div[3]/span[2]")
    stepname = (By.CLASS_NAME, "stepDesc")
    sms_context = (By.CLASS_NAME, "marketContentText")
    sms_interval = (By.CLASS_NAME, "sendInterval")
    btn_commit = (By.XPATH, "//*[@id='createShopTaskDialog']/div/div[3]/span[3]")
    first_rowname = (By.XPATH, "//*[@id='dataTable']/tbody/tr[1]/td[1]")

    def menu_click(self):
        menu1 = self.driver.find_element(*BaseTaskPage.m_tcenter)
        menu1.click()
        menu2 = self.driver.find_element(*BaseTaskPage.m_tshop)
        menu2.click()
        menu2 = self.driver.find_element(*BaseTaskPage.m_tshop_create)
        menu2.click()

    def task_create_click(self):
        btn = self.driver.find_element(*BaseTaskPage.btn_tshop_create)
        btn.click()

    def set_tname(self, tname):
        name = self.driver.find_elements(*BaseTaskPage.t_name)[0]
        tname = tname + time.strftime("%m%d%H%M%S")
        name.send_keys(tname)
        return tname

    def set_tbusiness(self, tbusiness):
        tbusiness_list = Select(self.driver.find_elements(*BaseTaskPage.t_business)[0])
        tbusiness_list.select_by_visible_text(tbusiness)

    def set_tbtime(self, btime):
        js = "$('input.startTime').removeAttr('readonly')"
        self.driver.execute_script(js)
        tbtime = self.driver.find_elements(*BaseTaskPage.t_btime)[0]
        tbtime.send_keys(btime)

    def set_tstime(self, stime):
        js = "$('input.stopTime').removeAttr('readonly')"
        self.driver.execute_script(js)
        tstime = self.driver.find_elements(*BaseTaskPage.t_stime)[0]
        tstime.send_keys(stime)

    def set_shop(self):
        shop = self.driver.find_elements(*BaseTaskPage.t_shop)[0]
        shop.click()
        shopchoose_btn = self.driver.find_element(*BaseTaskPage.btn_shop_choose)
        shopchoose_btn.click()
        confirm_btn = self.driver.find_element(*BaseTaskPage.btn_confirm)
        confirm_btn.click()

    def set_tdesc(self, desc):
        tdesc = self.driver.find_elements(*BaseTaskPage.t_desc)[0]
        tdesc.send_keys(desc)

    def next1_click(self):
        next1 = self.driver.find_element(*BaseTaskPage.btn_next1)
        next1.click()

    def get_stepname(self, step):
        steps = self.driver.find_elements(*BaseTaskPage.stepname)
        if step == 1:
            return steps[0].text
        if step == 2:
            return steps[1].text
        if step == 3:
            return steps[2].text
        if step == 4:
            return steps[3].text

    def set_sms(self, text):
        smstext = self.driver.find_elements(*BaseTaskPage.sms_context)[0]
        smstext.send_keys(text)

    def set_interval(self, interval):
        smsinterval = self.driver.find_elements(*BaseTaskPage.sms_interval)[0]
        smsinterval.send_keys(interval)

    def commit_click(self):
        commit = self.driver.find_element(*BaseTaskPage.btn_commit)
        commit.click()

    def get_rowname(self):
        firstrow = self.driver.find_element(*BaseTaskPage.first_rowname)
        return firstrow.text

    # 根据任务名称查找任务状态，用于ShopTaskAduit断言使用
    def get_task_state(self, tname):
        t_state = self.driver.find_element(By.XPATH, "//td[text()='" + tname + "']/../td[8]/i")
        return t_state.text
