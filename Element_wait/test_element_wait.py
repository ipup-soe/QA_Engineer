import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.mark.parametrize("elem", ["//input[@name='search']", "//div[@class='carousel-inner']",
                                  "//div[@class='col']", "//h3[text()='Featured']",
                                  "//ul[@class='nav navbar-nav']"])
def test_elements_main_page(browser, elem):
    browser.get("https://demo.opencart.com")
    assert browser.title == 'Your Store'
    try:
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, elem)))
    except TimeoutException:
        raise AssertionError(f"Элемент по локатору '{elem}' на странице не найден")

def test_elements_catalog_page(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(((By.XPATH, "//a[text()='Laptops & Notebooks']")))).click()
    wait.until(EC.visibility_of_element_located(((By.XPATH, "//a[text()='Show All Laptops & Notebooks']")))).click()
    wait.until(EC.visibility_of_element_located(((By.XPATH, "//h2[text()='Laptops & Notebooks']"))))
    wait.until(EC.visibility_of_element_located(((By.XPATH, "//aside[@id='column-left']"))))
    wait.until(EC.visibility_of_element_located(((By.XPATH, "//ul[@class='breadcrumb']"))))
    wait.until(EC.visibility_of_element_located(((By.ID, "display-control"))))
    wait.until(EC.visibility_of_element_located(((By.ID, "product-list"))))

def test_elements_card_page(browser):
    browser.get("https://demo.opencart.com")
    wait = WebDriverWait(browser, 5)
    feat_p = wait.until(EC.visibility_of_all_elements_located(((By.CSS_SELECTOR, "#content > div.row .product-thumb"))))[0]
    feat_p.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Add to Wish List']")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-quantity"))).clear()
    wait.until(EC.visibility_of_element_located((By.ID, "input-quantity"))).send_keys('12')
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Compare this Product']")))
    wait.until(EC.visibility_of_element_located((By.ID, "button-cart")))

def test_elements_login_adm_page(browser):
    browser.get("https://demo.opencart.com/admin/")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Username']")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-username"))).send_keys('test32112')
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-password"))).send_keys('pass32112')
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()=' Login']")))

def test_elements_reg_user_page(browser):
    browser.get("https://demo.opencart.com/index.php?route=account/register")
    assert browser.title == 'Register Account'
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located((By.ID, "content")))
    wait.until(EC.visibility_of_element_located((By.ID, "account")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-firstname"))).send_keys('D123hhfw')
    wait.until(EC.visibility_of_element_located((By.ID, "input-lastname"))).send_keys('D1wdasad')
    wait.until(EC.visibility_of_element_located((By.ID, "input-email"))).send_keys('D124dwfvaadsf3@hhfw.com')
    wait.until(EC.visibility_of_element_located((By.XPATH, "//legend[text()='Your Password']")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-password"))).send_keys('D124dwfvaadsf3hhfw')
    wait.until(EC.visibility_of_element_located((By.XPATH, "//legend[text()='Newsletter']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='checkbox']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Continue']")))
