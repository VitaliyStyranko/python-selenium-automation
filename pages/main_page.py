from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class MainPage(Page):

    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDER_BTN = (By.ID, "nav-orders")
    CART_ICON = (By.ID, "nav-cart")
    DEPARTMENT_SELECTION = (By.ID, "searchDropdownBox")
    NEW_ARRIVALS_SELECTION = (By.XPATH, "//div[@id='nav-subnav']//a[contains(@href,'New-Arrivals')]")
    NEW_ARRIVALS = (By.CSS_SELECTOR, '[class="mega-menu"]')


    def open_main(self):
        self.driver.get('https://www.amazon.com/')

    def clik_order_link(self):
        self.click(*self.ORDER_BTN)

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def click_on_cart_icon(self):
        self.click(*self.CART_ICON)

    def select_department(self, selection_value):
        select = Select(self.driver.find_element(*self.DEPARTMENT_SELECTION))
        select.select_by_value(f'search-alias={selection_value}')

    def click_on_search_btn(self):
        self.click(*self.SEARCH_BTN)

    def hover_new_arrival(self):
        new_arrival_selection = self.find_element(*self.NEW_ARRIVALS_SELECTION)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrival_selection)
        actions.perform()

    def verify_new_arrivals_options(self):
        self.wait_for_element_appear(*self.NEW_ARRIVALS)




sleep(10)