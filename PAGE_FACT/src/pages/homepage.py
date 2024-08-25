from seleniumpagefactory import PageFactory


class HomePage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
            "sign_in": ("ID", 'signin'),
            "user_name": ("CSS", ".username")
        }

    def click_sing_in(self):
        self.sign_in.click()

    def get_username(self):
        retr_username = self.user_name.get_text()
        assert retr_username == 'demouser'
