from selenium.webdriver.common.by import By

from POM.Src.PageObject.Locators import Locator


class Home:
    def __init__(self, driver):
        self.driver = driver
        self.contact = driver.find_element(By.XPATH, Locator.contact)

    def get_contact_button(self):
        return self.contact
