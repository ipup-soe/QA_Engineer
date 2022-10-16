from selenium.webdriver.common.by import By
from page_objects.page_o.Base_page import BasePage


class FeatureProduct(BasePage):
    FEATURED_PRODUCT = (By.CSS_SELECTOR, "#content > div.row .product-thumb")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".description h4 a")
    """#content > div.row .product-thumb .content .description h4 a"""


    def click_featured_product(self, index):
        feature_product = self.elements(self.FEATURED_PRODUCT)[index]
        # product_name = feature_product.find_element(*self.PRODUCT_NAME).text
        self.click(feature_product)
        # return product_name

    def get_product_name(self, index):
        product_name = self.elements(self.PRODUCT_NAME)[index].text
        return product_name
