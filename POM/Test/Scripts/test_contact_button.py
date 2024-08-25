import os
import sys
import unittest

from POM.Src.PageObject.Pages.HomePage import Home
from POM.Src.TestBase.WebDriverSetup import WebDriverSetup

sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())


class Contact_Button(WebDriverSetup):
    def test_contact_button(self):
        driver = self.driver
        self.driver.get('https://www.demoblaze.com/')
        self.driver.set_page_load_timeout(30)

        home = Home(driver)
        home.contact.click()
        self.driver.save_screenshot("contact_button_test.png")

if __name__ == '__main__':
    unittest.main()