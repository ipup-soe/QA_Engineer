from selenium.webdriver.common.by import By
from page_objects.page_o.Base_page import BasePage


class NaviPage(BasePage):
    CURRENCY = (By.XPATH, "//span[@class='d-none d-md-inline' and text()='Currency']")
    WICH_LIST = (By.ID, "wishlist-total")
    SHOPPING_CART = (By.XPATH, "//li[@class='list-inline-item']/a[@title='Shopping Cart']")
    MY_ACCOUNT = (By.XPATH, "//span[text()='My Account']")
    CHECK_CART = (By.CSS_SELECTOR, 'div#header-cart')
    REGISTER = (By.XPATH, "//a[text()='Register']")

    def click_currency(self):
        self.click(self.element(self.CURRENCY))

    def click_wich_list(self):
        self.click(self.element(self.WICH_LIST))

    def click_shopping_cart(self):
        self.click(self.element(self.SHOPPING_CART))

    def check_shopping_cart(self):
        check = self.element(self.CHECK_CART).text
        check = int(check[0])
        return check

    def check_shopping_currency(self):
        check = self.element(self.CHECK_CART).text
        print(check)

    def click_register(self):
        self.click(self.element(self.MY_ACCOUNT))
        self.click(self.element(self.REGISTER))
