from selenium.webdriver.common.by import By
from page_objects.page_o.Base_page import BasePage


class ProductPage(BasePage):
    WISH_LIST = (By.CSS_SELECTOR, "[data-bs-original-title='Add to Wish List']")
    COMPARE = (By.CSS_SELECTOR, "[data-bs-original-title='Compare this Product']")
    CART = (By.ID, "button-cart")

    def add_to_wish_list(self):
        self.click(self.element(self.WISH_LIST))

    def add_to_comparison(self):
        self.click(self.element(self.COMPARE))

    def add_to_cart(self):
        self.click(self.element(self.CART))
