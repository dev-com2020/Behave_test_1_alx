from seleniumpagefactory import PageFactory


class SignUpPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
            'full_name': ('ID', 'user_full_name'),
            'business_email': ('ID', "user_email_login"),
            'password': ('ID', 'user_password'),
            'tnc': ('ID', 'tnc_checkbox'),
            'sign_up': ('ID', 'user_submit'),
            'accept_all': ('ID', 'accept-cookie-notification')
        }

    def enter_full_name(self):
        self.full_name.set_text("TestUser")

    def enter_business_emial(self):
        self.business_email.set_text("TestUser@business.com")

    def click_accept_notification(self):
        self.accept_all.click()

    def enter_password(self):
        self.password.set_text("TestPassword")

    def click_tnc(self):
        self.tnc.click()

    def click_signup(self):
        self.sign_up.click()
