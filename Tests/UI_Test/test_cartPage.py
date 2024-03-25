import time
from telnetlib import EC

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from Tests.UI_Test.BaseTest import BaseTest
from Pages.cartPage import CartPage
from Pages.loginPage import LoginPage
from Tests.configtest import init_driver, assertion_data,login_data
import pytest


class TestCart(BaseTest):

    @pytest.mark.run(order=3)
    def test_add_to_cart(self, setup_pages, login_data, assertion_data):
        driver, login_page, cart_page, _ = setup_pages
        self.login_and_assert(login_page, driver, login_data, assertion_data)
        cart_page.select_product()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(cart_page.product_name_div_locator))
            print("Product 'Sauce Labs Backpack' is present")
        except TimeoutException:
            print("Product 'Sauce Labs Backpack' is not present within the timeout period")
            assert False
        cart_page.add_to_cart()
        cart_page.click_cart_icon()
        cart_page.checking_productIn_cart(assertion_data["product_name"])
        cart_page.logout_page()

    @pytest.mark.run(order=4)
    def test_remove_from_cart(self, setup_pages, login_data, assertion_data):
        driver, login_page, cart_page, _ = setup_pages
        self.login_and_assert(login_page, driver, login_data, assertion_data)
        cart_page.select_product()
        cart_page.add_to_cart()
        cart_page.remove_product_from_cart(assertion_data["product_name"])
