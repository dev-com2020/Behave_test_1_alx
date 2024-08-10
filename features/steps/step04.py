from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@given('wchodzimy na strone madison island')
def step_open_webstore(context):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(options=options)
    context.driver.get("http://demo-store.seleniumacademy.com/")


@when('uzytkownik wpisuje w pole wyszukiwania "{query}"')
def step_search_product(context, query):
    search_box = context.driver.find_element(By.NAME, "q")
    search_box.send_keys(query)


@when('klika w przycisk szukaj')
def step_click(context):
    search_box = context.driver.find_element(By.NAME, "q")
    search_box.send_keys(Keys.ENTER)


@when('robie screenshot')
def step_take_screenshot(context):
    context.driver.save_screenshot('results.png')


@then('strona zawiera tresc "{expected_text}"')
def step_verify(context, expected_text):
    title = context.driver.title
    print(f"Tytuł strony: {title}")
    print(f"expected_text: {expected_text}")
