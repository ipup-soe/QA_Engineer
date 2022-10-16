import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_wish_list(browser):
    feature_product = browser.find_elements_by_css_selector("#content > div.row .product-thumb")[0]
    product_name = feature_product.find_element_by_css_selector(".description h4 a").text
    feature_product.click()
    print(product_name)