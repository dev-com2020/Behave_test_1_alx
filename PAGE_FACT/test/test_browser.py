from selenium import webdriver

from PAGE_FACT.src.pages.homepage import HomePage
from PAGE_FACT.src.pages.sign_in_page import SignInPage


def test_browser():
    driver = webdriver.Firefox()
    driver.get("https://bstackdemo.com/")

    homepage = HomePage(driver)
    sign_in_page = SignInPage(driver)

    homepage.click_sing_in()
    sign_in_page.select_username()
    sign_in_page.select_password()
    sign_in_page.click_login()
    homepage.get_username()

    driver.quit()