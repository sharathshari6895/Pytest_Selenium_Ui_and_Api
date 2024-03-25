import pytest
from Tests.UI_Test.BaseTest import BaseTest
from Pages.loginPage import LoginPage
from Tests.configtest import init_driver, login_data, assertion_data
import logging

class TestLogin(BaseTest):
    @pytest.mark.run(order=1)
    def test_invalid_password(self, setup_pages, login_data, assertion_data):
        driver, login_page, _, _ = setup_pages
        login_page.click_login(login_data['userName'], login_data['INVALID PASSWORD'])
        assert driver.current_url != assertion_data['expected_url']

    @pytest.mark.run(order=2)
    def test_valid_signin(self, setup_pages, login_data, assertion_data):
        driver, login_page, _, _ = setup_pages
        self.login_and_assert(login_page, driver, login_data, assertion_data)
