from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")
SEARCH_RESULTS = (By.CSS_SELECTOR,'[data-component-type="s-search-result"]')
PRODUCT_TITLE = (By.CSS_SELECTOR,'h2 span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, '.s-image[data-image-latency="s-product-image"]')


@given('Open the Amazon product {product_id} page')
def open_amazon_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')


@then ('Verify the user can switch between colors')
def verify_user_can_click_color(context):
    expected_colors = ['Black', 'Blue, Over Dye', 'Dark Blue Vintage']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:3]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]
    assert expected_colors == actual_colors,\
        f'Expected colors {expected_colors} did not match actual {actual_colors}'


@then('Verify that every product has a name and an image')
def verify_products_name_image(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Error.Title should not be blank'
        product.find_element(*PRODUCT_IMG)




