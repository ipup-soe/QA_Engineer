from selenium.webdriver.common.by import By
from page_objects.page_o.Base_page import BasePage


class CartPage(BasePage):
    DELL_PRODUCT = (By.CSS_SELECTOR, "div.input-group button.btn.btn-danger")

    def dell_product(self):
        self.click(self.element(self.DELL_PRODUCT))
