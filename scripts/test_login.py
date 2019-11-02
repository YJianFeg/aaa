import time

from base.base_driver import init_driver
from page.home_page import HomePage
from page.login_home_page import LoginHomePage
from page.me_home_page import MeHomePage
from page.me_page import MePage


class TestLogin:
    def setup(self):
        self.driver = init_driver()

        self.home_page = HomePage(self.driver)
        self.login_home_page = LoginHomePage(self.driver)
        self.me_page = MePage(self.driver)
        self.me_home_page = MeHomePage(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_login(self):
        self.home_page.click_me()
        self.me_page.click_have_login()
        self.login_home_page.input_user('itfeat')
        self.login_home_page.input_pw('itfeat123000')
        self.login_home_page.click_login_button()
        assert self.me_home_page.get_user() == 'itfeat'


