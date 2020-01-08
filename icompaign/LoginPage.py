from BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    c_btn = (By.CLASS_NAME, "login-change-icon")
    username = (By.ID, 'loginName')
    password = (By.ID, 'password')
    vcode = (By.CLASS_NAME, 'verificationText')
    # page_title = (By.XPATH, '//html/head/title')
    signButton = (By.CLASS_NAME, 'login')

    def click_change(self):
        btn = self.driver.find_element(*LoginPage.c_btn)
        btn.click()

    def set_username(self, username):
        name = self.driver.find_element(*LoginPage.username)
        name.send_keys(username)

    def set_password(self, password):
        pwd = self.driver.find_element(*LoginPage.password)
        pwd.send_keys(password)

    def set_verif(self, vcode):
        vc = self.driver.find_elements(*LoginPage.vcode)[1]
        vc.send_keys(vcode)

    def get_title(self):
        # title = self.driver.find_element(*LoginPage.page_title)
        return self.driver.title

    def click_sign(self):
        signbtn = self.driver.find_elements(*LoginPage.signButton)[1]
        signbtn.click()

    def login_icompaign(self, username, password):
        btn = self.driver.find_element(*LoginPage.c_btn)
        btn.click()
        name = self.driver.find_element(*LoginPage.username)
        name.send_keys(username)
        pwd = self.driver.find_element(*LoginPage.password)
        pwd.send_keys(password)
        vc = self.driver.find_elements(*LoginPage.vcode)[1]
        vc.send_keys("yyhh")
        signbtn = self.driver.find_elements(*LoginPage.signButton)[1]
        signbtn.click()
