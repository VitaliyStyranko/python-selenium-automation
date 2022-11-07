from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


@when('Click on cart icon')
def click_on_cart_icon(context):
     context.app.main_page.click_on_cart_icon()


@then("Verify 'Your Shopping Cart is empty.' text present")
def verify_Your_Amazon_Cart_is_empty_visible(context):
    context.app.shopping_cart_page.verify_Your_Amazon_Cart_is_empty_visible()
