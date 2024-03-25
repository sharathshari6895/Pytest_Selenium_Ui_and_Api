from Action.action import Events
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException


class CartPage(Events):
    selectProduct_locator = (By.XPATH, "//img[@alt='Sauce Labs Backpack']")
    addToCartBtn_locator = (By.XPATH, "//button[text()='Add to cart']")
    removeFromCartBtn_locator = (By.XPATH, "//button[text()='Remove']")
    shoppingCartBadge_locator = (By.XPATH, "//span[@class='shopping_cart_badge']")
    shoppingCartIcon_locator = (By.XPATH, "//a[@class='shopping_cart_link']")
    description_div_locator = (By.XPATH, "//div[@class='inventory_details_desc_container']")
    product_name_div_locator = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    check_productName_in_cart_locator = (By.XPATH, "//div[@id='cart_contents_container']")
    toggle_menu_locator = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    logout_button_locator = (By.XPATH, "//a[@id='logout_sidebar_link']")
    cart_items_locator = (By.XPATH, "//div[@class='cart_item']")
    # product_name_xpath = ".//div[@class='inventory_item_name']"
    remove_button_xpath = ".//button[text()='Remove']"

    def __init__(self, driver):
        super().__init__(driver)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def select_product(self):
        self.do_click(self.selectProduct_locator)

    def add_to_cart(self):
        description_div_element = self.find_element(self.description_div_locator)
        if "Add to cart" in description_div_element.text:
            self.do_click(self.addToCartBtn_locator)
            print("clicked on Add to cart")

    def click_cart_icon(self):
        self.do_click(self.shoppingCartIcon_locator)

    def checking_productIn_cart(self, productName):
        description_div_element = self.find_element(self.check_productName_in_cart_locator)
        if productName in description_div_element.text:
            print("Add to Cart successfully")

    def logout_page(self):
        self.do_click(self.toggle_menu_locator)
        self.do_click(self.logout_button_locator)

    def remove_product_from_cart(self, productName):
        try:
            # Check if the shopping cart badge locator is present
            self.driver.find_element(*self.shoppingCartBadge_locator)
        except NoSuchElementException:
            print("Shopping cart badge not found. Exiting function.")
            return

        # If shopping cart badge is present, proceed with the rest of the logic
        try:
            cart_item_count = int(self.driver.find_element(*self.shoppingCartBadge_locator).text)
            if cart_item_count <= 0:
                print("Cart Item is empty")
            else:
                self.do_click(self.shoppingCartIcon_locator)
                cart_items = self.find_elements(self.cart_items_locator)
                for cart_item in cart_items:
                    productNameToRemove = cart_item.find_element(By.XPATH, self.product_name_xpath).text
                    if productName in productNameToRemove:
                        remove_button = cart_item.find_element(By.XPATH, self.remove_button_xpath)
                        remove_button.click()
                        print("CartItem is removed")
                        break
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

