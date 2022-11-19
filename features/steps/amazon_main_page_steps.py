from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC



@given('Open amazon page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('Click Amazon Orders link')
def clik_order_link(context):
    context.app.main_page.clik_order_link()


@when('Select department by value {selection_value}')
def select_department(context, selection_value):
    context.app.main_page.select_department(selection_value)


@then('Search for {product}')
def search_product(context, product):
    context.app.main_page.search_product(product)


@then('Click on search btn')
def click_on_search_btn(context):
    context.app.main_page.click_on_search_btn()


@then('Verify {department} department is selected')
def verify_department(context, department):
    context.app.search_result_page.verify_department(department)




