from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MeHomePage(BaseAction):
    user_nikename = By.ID, 'com.yunmall.lc:id/tv_user_nikename'

    def get_user(self):
        return self.get_text(self.user_nikename)