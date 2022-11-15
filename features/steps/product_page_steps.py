from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains


@given('Open Amazon product {product_id} page')
def open_amazon_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')


@when('Hover over New Arrivals options')
def hover_new_arrivals(context):
    context.app.main_page.hover_new_arrival()


@then('Verify New Arrivals options present')
def verify_new_arrivals_options(context):
    context.app.main_page.verify_new_arrivals_options()
