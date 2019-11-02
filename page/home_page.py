from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    me_button = By.ID, 'com.yunmall.lc:id/tab_me'

    def click_me(self):
        self.click(self.me_button)

    # 如果没有登录就登录
    def login_if_not(self, page):
        """
        调用之后会来到我的界面，并保持登录状态
        :param page:
        :return:
        """
        # 在首页中，点击我
        self.click_me()
        # 当前页面的名字，是否等于 "注册"页面的名字
        if self.driver.current_activity == "com.yunmall.ymctoc.ui.activity.LogonActivity":
            # 如果相等，则没有登录
            # 点击已有账号去登陆
            page.me.click_have_login()
            # 输入用户名
            page.login_home.input_user("itfeat")
            # 登陆 输入 密码
            page.login_home.input_pw("itfeat123000")
            # 登陆 点击 登陆
            page.login_home.click_login_button()
