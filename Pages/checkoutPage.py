from Action.action import Events
from selenium.webdriver.common.by import By


class CheckoutPage(Events):
    shoppingCartIcon_locator = (By.XPATH, "//a[@class='shopping_cart_link']")
    checkoutBtn_locator = (By.XPATH, "//button[text()='Checkout']")
    firstName_input = (By.XPATH, "//input[@id='first-name']")
    lastName_input = (By.XPATH, "//input[@id='last-name']")
    zipCode_input = (By.XPATH, "//input[@id='postal-code']")
    continue_checkout_btn = (By.XPATH, "//input[@id='continue']")
    finish_checkout_btn = (By.XPATH, "//button[@id='finish']")
    click_select_dropdown = (By.XPATH, "//select[@class='product_sort_container']")
    select_option = (By.XPATH, "//option[@value='lohi']")
    product_price_locator = (By.XPATH, "//div[@class='inventory_item_price']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_cart_icon(self):
        self.do_click(self.shoppingCartIcon_locator)

    def click_checkout(self):
        self.do_click(self.checkoutBtn_locator)

    def checkout_details(self, firstname, lastname, zipcode):
        self.do_send_keys(self.firstName_input, firstname)
        self.do_send_keys(self.lastName_input, lastname)
        self.do_send_keys(self.zipCode_input, zipcode)

    def continue_checkout(self):
        self.do_click(self.continue_checkout_btn)

    def finish_checkout(self):
        self.do_click(self.finish_checkout_btn)

    def select_dropdown(self):
        self.do_click(self.click_select_dropdown)
        self.do_click(self.select_option)

    def compare_product_prices(self):
        price_elements = self.driver.find_elements(*self.product_price_locator)
        prices = [price_element.text.strip('$') for price_element in price_elements[:2]]
        numeric_prices = [float(price) for price in prices]
        if numeric_prices[1] >= numeric_prices[0]:
            print("The price of the second product is higher or equal to the first product.")
        else:
            print("The price of the second product is lower than the first product.")
