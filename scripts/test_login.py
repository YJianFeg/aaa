import time

import pytest

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize('args', analyze_data('login_data.yaml', 'test_login'))
    def test_login(self, args):
        username = args['username']
        password = args['password']
        expect = args['expect']

        self.page.home.click_me()
        self.page.me.click_have_login()
        self.page.login_home.input_user(username)
        self.page.login_home.input_pw(password)
        self.page.login_home.click_login_button()

        if expect is None:
            assert self.page.me_home.get_user() == username
        else:
            assert self.page.me_home.is_toast_exist(expect)


