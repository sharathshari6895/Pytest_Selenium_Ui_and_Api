import pytest
from Pages.loginPage import LoginPage
from Pages.cartPage import CartPage
from Pages.checkoutPage import CheckoutPage


# parent class for all test classes
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    @pytest.fixture(scope="function")
    def setup_pages(self, init_driver):
        driver = init_driver
        login_page = LoginPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        return driver, login_page, cart_page, checkout_page

    @staticmethod
    def login_and_assert(login_page, driver, login_data, assertion_data):
        login_page.click_login(login_data['userName'], login_data['PASSWORD'])
        print(driver.current_url)
        assert driver.current_url == assertion_data['expected_url']