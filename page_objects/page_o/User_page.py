from selenium.webdriver.common.by import By
from page_objects.page_o.Base_page import BasePage


class UserPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value=Login]")
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    PRIVACY_POLLICY = (By.CSS_SELECTOR, "div.float-end input.form-check-input")
    CONTINUE = (By.XPATH, "//button[text()='Continue']")
    VERYFY = (By.XPATH, "//h1[text()='Your Account Has Been Created!']")

    def login(self, username, password):
        self._input(self.element(self.EMAIL_INPUT), username)
        self._input(self.element(self.PASSWORD_INPUT), password)
        self.click(self.element(self.LOGIN_BUTTON))
        return self

    def regis(self, first_name, last_name, email,password):
        self._input(self.element(self.FIRST_NAME), first_name)
        self._input(self.element(self.LAST_NAME), last_name)
        self._input(self.element(self.EMAIL_INPUT), email)
        self._input(self.element(self.PASSWORD_INPUT), password)
        self.click(self.element(self.PRIVACY_POLLICY))
        self.click(self.element(self.CONTINUE))

    def verify_add_account(self):
        self.element(self.VERYFY)
