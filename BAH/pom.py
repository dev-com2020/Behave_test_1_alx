import unittest

import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By


class demoblazeTest(unittest.TestCase):

    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def test_product(self):
        driver_chrome = webdriver.Chrome()
        self.driver = driver_chrome
        driver_chrome.get('https://www.demoblaze.com/')
        elem = driver_chrome.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[2]/a')
        elem.click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
