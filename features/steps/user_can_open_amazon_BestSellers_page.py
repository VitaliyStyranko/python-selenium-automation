from selenium.webdriver.common.by import By
from behave import given, when, then


BEST_SELLER_PAGE = (By. CSS_SELECTOR, "div[class*='p13n-zg-nav-tab-all_style_zg-tabs-li']")


@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Best Sellers button')
def click_on_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()


@then('Verify header has {expected_link_count} links')
def verify_links_count(context, expected_link_count):
    expected_link_count = int(expected_link_count)
    links = context.driver.find_elements(*BEST_SELLER_PAGE)
    assert len(links) == expected_link_count, \
        f'Expected {expected_link_count} links, but got {len(links)}'
