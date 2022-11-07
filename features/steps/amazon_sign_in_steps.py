from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


@given('Open amazon page')
def open_amazon(context):
    context.app.main_page.open_main()

@when('Click Amazon Orders link')
def clik_order_link(context):
    context.app.main_page.clik_order_link()

@then('Verify Sign In page is opened')
def verify_sign_in_header_is_visible(context):
      context.app.sign_in_page.verify_sign_in_header_is_visible()
