from base.base_driver import init_driver


class TestLogin:
    def setup(self):
        self.driver = init_driver()

    def test_he(self):
        print('HELlO')
