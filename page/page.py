from page.home_page import HomePage
from page.login_home_page import LoginHomePage
from page.me_home_page import MeHomePage
from page.me_page import MePage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def login_home(self):
        return LoginHomePage(self.driver)

    @property
    def me(self):
        return MePage(self.driver)

    @property
    def me_home(self):
        return MeHomePage(self.driver)



