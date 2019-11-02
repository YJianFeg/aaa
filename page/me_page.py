from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):
    have_login_button = By.ID, 'com.yunmall.lc:id/textView1'

    def click_have_login(self):
        self.click(self.have_login_button)