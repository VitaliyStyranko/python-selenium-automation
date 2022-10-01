from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Cart icon')
def click_on_icon(context):
    context.driver.find_element(By.ID, "nav-cart").click()


@then('Verifies Your Amazon Cart is empty visible')
def verify_Your_Amazon_Cart_is_empty_visible(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']").text
    assert actual_result == expected_result, f'Error! Expected {expected_result}, but got {actual_result}'

