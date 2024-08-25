import unittest

from POM.Src.PageObject.Pages.HomePage import Home
from POM.Src.TestBase.WebDriverSetup import WebDriverSetup


class DemoBlazeHomePage(WebDriverSetup):
    def test_Home_Page(self):
        driver = self.driver
        self.driver.get('https://www.demoblaze.com/')
        self.driver.set_page_load_timeout(30)

        web_page_title = "STORE"

        try:
            if driver.title == web_page_title:
                print("WebPage loaded...")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error, "WebPage failed!")

        home_page = Home(driver)

if __name__ == '__main__':
    unittest.main()