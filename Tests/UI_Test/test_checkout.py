import pytest
from Pages.checkoutPage import CheckoutPage
from Pages.cartPage import CartPage
from Pages.loginPage import LoginPage
from Tests.UI_Test.BaseTest import BaseTest
from Tests.configtest import init_driver, assertion_data, login_data


class TestCheckout(BaseTest):

    @pytest.mark.run(order=5)
    def test_checkout(self, setup_pages, login_data, assertion_data):
        driver, login_page, cart_page, checkout_page = setup_pages
        self.login_and_assert(login_page, driver, login_data, assertion_data)
        cart_page.select_product()
        cart_page.add_to_cart()
        cart_page.click_cart_icon()
        checkout_page.click_checkout()
        checkout_page.checkout_details(login_data['firstName'], login_data['lastName'], login_data['Zipcode'])
        checkout_page.continue_checkout()
        checkout_page.finish_checkout()
        print("Checkout Successful")

    @pytest.mark.run(order=6)
    def test_sort_products(self, setup_pages, login_data, assertion_data):
        driver, login_page, _, checkout_page = setup_pages
        self.login_and_assert(login_page, driver, login_data, assertion_data)
        checkout_page.select_dropdown()
        checkout_page.compare_product_prices()
        print("option selected")
