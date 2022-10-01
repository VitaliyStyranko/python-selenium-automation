from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Return & Order button')
def click_on_button(context):
    context.driver.find_element(By.ID, "nav-orders").click()
    
    
@then('Verify Sign in header is visible')
def verify_Sign_in_header_visible(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert actual_result == expected_result, f'Error! Expected {expected_result}, but got {actual_result}'


@then('Verify email input field is present')
def verify_email_input_field_is_present(context):
    assert context.driver.find_element(By.ID, "ap_email").is_displayed(), 'Email field not shown'
    
    
 
    