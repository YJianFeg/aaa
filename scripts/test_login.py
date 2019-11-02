import time

from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_login(self):
        self.page.home.click_me()
        self.page.me.click_have_login()
        self.page.login_home.input_user('itfeat')
        self.page.login_home.input_pw('itfeat123000')
        self.page.login_home.click_login_button()
        assert self.page.me_home.get_user() == 'itfeat'


