from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


PRIVACY_NOTICE = (By.XPATH, '//a[contains(@class,"help-display-cond") and text()="Privacy Notice"]')


@given('Open Amazon T&C page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    # print('Original: ', context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    # print("Current windows: ", current_windows)
    context.driver.switch_to.window(current_windows[1])


@then("Verify Amazon Privacy Notice page is opened")
def verify_privacy_notice_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))
    # print("Current windows: ", context.driver.current_window_handle)


@then('User can close new window and switch back to original')
def close_new_and_switch_to_original_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)








