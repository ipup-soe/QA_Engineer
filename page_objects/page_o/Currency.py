from selenium.webdriver.common.by import By
from page_objects.page_o.Base_page import BasePage


class Currency(BasePage):
    CURRENCY_SYMBOL = (By.XPATH, "//strong")
    CURRENCY = (By.CSS_SELECTOR, "span.d-none+i.fas")
    EURO = (By.XPATH, "//a[text()='€ Euro']")
    POUNT_STERLING = (By.XPATH, "//a[text()='£ Pound Sterling']")
    USD = (By.XPATH, "//a[text()='$ US Dollar']")

    def сurrency_euro(self):
        self.click(self.element(self.CURRENCY))
        curr_symb = self.element(self.EURO).text
        self.click(self.element(self.EURO))
        return curr_symb[0]

    def сurrency_pount(self):
        self.click(self.element(self.CURRENCY))
        curr_symb = self.element(self.POUNT_STERLING).text
        self.click(self.element(self.POUNT_STERLING))
        return curr_symb[0]

    def сurrency_usd(self):
        self.click(self.element(self.CURRENCY))
        curr_symb = self.element(self.USD).text
        self.click(self.element(self.USD))
        return curr_symb[0]

    def check_currency(self):
        curr = self.element(self.CURRENCY_SYMBOL).text
        return curr
