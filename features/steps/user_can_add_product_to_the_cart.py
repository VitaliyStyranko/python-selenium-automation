from selenium.webdriver.common.by import By
from behave import given, when, then


PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-impression-logger']//a[.//span[@class='a-price-whole']]")
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART_PAGE = (By.ID, 'nav-cart')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {product}')
def search_product(context, product):
    element = context.driver.find_element(By.ID, "twotabsearchtextbox")
    element.clear()
    element.send_keys(product)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@then('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@then('Open cart page')
def click_on_icon(context):
    context.driver.find_element(*CART_PAGE).click()


@then('Verify product added to the cart')
def verify_Subtotal_items(context):
    assert context.driver.find_element(By.ID, "sc-subtotal-label-buybox").is_displayed(), 'Subtotal not shown'
