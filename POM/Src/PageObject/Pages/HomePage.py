import os
import sys

from selenium.webdriver.common.by import By

from POM.Src.PageObject.Locators import Locator

sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

class Home:
    def __init__(self, driver):
        self.driver = driver
        self.contact = driver.find_element(By.XPATH, Locator.contact)

    def get_contact_button(self):
        return self.contact
