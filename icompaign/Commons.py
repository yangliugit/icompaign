from BasePage import BasePage
import time


class Commons(BasePage):

    def exception_picture(self, methodname):
        filename = methodname + time.strftime("%Y%m%d%H%M%S")
        self.driver.get_screenshot_as_file("F:\icompaign\picture\%s.png" % filename)
