# -*- coding: utf-8 -*-
from BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class ShopTaskPoolPage(BasePage):
    m_tcenter = (By.ID, "60")
    m_tshop = (By.ID, "70")
    m_tpool = (By.ID, "74")
    first_task_name = (By.XPATH, "//*[@id='dataTable']/tbody/tr[1]/td[1]")
    btn_execute = (By.ID, "btnSuccess")
    box_taskname = (By.CLASS_NAME, "detail_taskName")
    btn_confirm = (By.CLASS_NAME, "layui-layer-btn0")
    btn_cancel = (By.CLASS_NAME, "layui-layer-btn1")
    execute_state = (By.XPATH, "//*[@id='dataTable']/tbody/tr/td[9]/i")

    def pool_menu_click(self):
        menu1 = self.driver.find_element(*ShopTaskPoolPage.m_tcenter)
        menu1.click()
        menu2 = self.driver.find_element(*ShopTaskPoolPage.m_tshop)
        menu2.click()
        menu3 = self.driver.find_element(*ShopTaskPoolPage.m_tpool)
        time.sleep(1)
        menu3.click()

    def get_first_task_name(self):
        firsttask = self.driver.find_element(*ShopTaskPoolPage.first_task_name)
        return firsttask.text

    def execute_task(self):
        btnexecute = self.driver.find_elements(*ShopTaskPoolPage.btn_execute)[0]
        btnexecute.click()

    def get_box_taskname(self):
        boxtaskname = self.driver.find_elements(*ShopTaskPoolPage.box_taskname)[0]
        return boxtaskname.text

    def execute_confirm(self):
        btnconfirm = self.driver.find_element(*ShopTaskPoolPage.btn_confirm)
        btnconfirm.click()

    def get_state(self):
        state = self.driver.find_elements(*ShopTaskPoolPage.execute_state)[0]
        return state.text
