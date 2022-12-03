from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):

    def verify_sign_in_header_is_visible(context):
        expected_result = 'Sign in'
        actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
        assert actual_result == expected_result, f'Error! Expected {expected_result}, but got {actual_result}'


