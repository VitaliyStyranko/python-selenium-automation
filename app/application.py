from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.shopping_cart_page import ShoppingCart
from pages.search_result_page import SearchResultPage


class Application:


    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.shopping_cart_page = ShoppingCart(self.driver)
        self.search_result_page = SearchResultPage(self.driver)
