from page_objects.page_o.Feature_product import FeatureProduct
from page_objects.page_o.ProductPage import ProductPage
from page_objects.page_o.Navi_page import NaviPage
from page_objects.page_o.Base_page import BasePage
from page_objects.page_o.Cart_page import CartPage
from page_objects.page_o.User_page import UserPage
from page_objects.test_data.users import get_user
from page_objects.page_o.Currency import Currency


def test_add_new_product(browser):
    """добавление нового товара"""
    product_name = FeatureProduct(browser).get_product_name(0)
    FeatureProduct(browser).click_featured_product(0)
    ProductPage(browser).add_to_cart()
    NaviPage(browser).click_shopping_cart()
    BasePage(browser).verify_product_item(product_name)

def test_del_product(browser):
    """Удаление товара"""
    if NaviPage(browser).check_shopping_cart() != 0:
        NaviPage(browser).check_shopping_cart()
        CartPage(browser).dell_product()
    else: pass

def test_reg_new_user(browser):
    """Регистрация нового пользователя"""
    NaviPage(browser).click_register()
    UserPage(browser).regis(*get_user())
    assert UserPage(browser).verify_add_account()

def test_curr_switc(browser):
    """Переключение валют"""
    assert Currency(browser).сurrency_euro() == Currency(browser).check_currency()
    assert Currency(browser).сurrency_pount() == Currency(browser).check_currency()
    assert Currency(browser).сurrency_usd() == Currency(browser).check_currency()
