from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Resources.Locators import Locators
from Tests.TestData import TestData
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # performs click on web element whose locator is passed to
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    # performs comparison of a web element text and the input text
    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()


class HomePage(BasePage):
    """ Home page of Amazon """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def search(self):
        self.driver.find_element(*Locators.SEARCH_TEXTBOX).clear()
        self.enter_text(Locators.SEARCH_TEXTBOX, TestData.SEARCH_TERM)
        self.click(Locators.SEARCH_SUBMIT_BUTTON)


class SearchResultsPage(BasePage):
    """Search Results Page of Amazon"""
    def __init__(self, driver):
        super().__init__(driver)

    def click_search_result(self):
        self.click(Locators.SEARCH_RESULT_LINK)


class ProductDetailsPage(BasePage):
    """Product detail when click an item to cart"""
    def __init__(self, driver):
        super().__init__(driver)

    def click_add_item_to_cart(self):
        self.click(Locators.ADD_TO_CART_BUTTON)


class SubCartPage(BasePage):
    """Sub Cart Page of Amazon"""
    def __init__(self, driver):
        super().__init__(driver)

    def click_cart_link(self):
        self.click(Locators.CART_LINK)


class CartPage(BasePage):
    """Cart Page on Amazon """

    def __init__(self, driver):
        super().__init__(driver)

    def click_proceed_to_checkout_button(self):
        self.click(Locators.PROCEED_TO_CHECKOUT_BUTTON)

    def delete_item(self):
        cartCount = int(self.driver.find_element(*Locators.CART_COUNT).text)
        if cartCount < 1:
            print("Cart is Empty")
            exit()

        if self.driver.title.startswith(TestData.SHOPPING_CART_TITLE):
            self.click(Locators.DELETE_ITEM_LINK)
            time.sleep(2)


class SignInPage(BasePage):
    """SignIn Page on Amazon """

    def __init__(self, driver):
        super().__init__(driver)

