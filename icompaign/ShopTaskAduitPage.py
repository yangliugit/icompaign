# -*- coding: utf-8 -*-
from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ShopTaskAuditPage(BasePage):
    m_pcenter = (By.ID, "82")
    m_shop_audit = (By.ID, "86")
    first_task_name = (By.XPATH, "//*[@id='dataTable']/tbody/tr[1]/td[2]")
    btn_first_audit = (By.CLASS_NAME, "btn-sm")
    audit_select = (By.ID, "auditDecision")
    btn_confirm = (By.CLASS_NAME, "layui-layer-btn0")
    btn_cancel = (By.CLASS_NAME, "layui-layer-btn1")
    input_reason = (By.ID, "reason")

    def menu_click(self):
        menu1 = self.driver.find_element(*ShopTaskAuditPage.m_pcenter)
        menu1.click()
        menu2 = self.driver.find_element(*ShopTaskAuditPage.m_shop_audit)
        menu2.click()

    # 获取任务名称用于判断其为自动化任务
    def get_first_task_name(self):
        firsttask = self.driver.find_element(*ShopTaskAuditPage.first_task_name)
        return firsttask.text

    def audit_click(self):
        auditbtn = self.driver.find_elements(*ShopTaskAuditPage.btn_first_audit)[0]
        auditbtn.click()

    def audit(self, result="pass", reason="Test pass"):
        sel = self.driver.find_element(*ShopTaskAuditPage.audit_select)
        btnconfirm = self.driver.find_element(*ShopTaskAuditPage.btn_confirm)
        inputreason = self.driver.find_element(*ShopTaskAuditPage.input_reason)
        if result == "pass":
            Select(sel).select_by_value("0")
            inputreason.send_keys(reason)
            btnconfirm.click()
        else:
            Select(sel).select_by_value("1")
            inputreason.send_keys(reason)
            btnconfirm.click()
