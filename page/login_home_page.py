from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginHomePage(BaseAction):
    user_text = By.ID, 'com.yunmall.lc:id/logon_account_textview'
    pw_text = By.ID, 'com.yunmall.lc:id/logon_password_textview'
    login_button = By.XPATH, '//*[@text="登录"]'

    def input_user(self, text):
        self.input(self.user_text, text)

    def input_pw(self, text):
        self.input(self.pw_text, text)

    def click_login_button(self):
        self.click(self.login_button)