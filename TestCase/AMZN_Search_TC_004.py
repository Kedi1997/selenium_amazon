import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

"""
TC4: User should be able to delete item from cart
"""


class DeleteItemFromCart(unittest.TestCase):
    base_url = "https://www.amazon.in"
    search_term = "How Google Works"

    # -- Pre - Condition --
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/pengkedi/Documents/selenium/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # -- Steps for AMZN_Search_TC_004 --
    def test_AMZN_Search_TC_004_delete_item_from_cart(self):
        """User should be able to delete an item from cart"""
        driver = self.driver
        driver.get(self.base_url)
        search_text_box = driver.find_element_by_id("twotabsearchtextbox")
        search_text_box.clear()
        search_text_box.send_keys(self.search_term)
        search_text_box.send_keys(Keys.RETURN)

        # to click the first search result's link
        driver.find_element_by_xpath(
            "(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]").click()

        # switch to new window tab since the result is opened in new tab
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_id("add-to-cart-button").click()
        # to confirm if the cart is empty
        print(driver.find_element_by_id('nav-cart-count').text)
        cart_count = int(driver.find_element_by_id("nav-cart-count").text)
        if cart_count < 1:
            print("Cart is Empty")
            exit()

        # click the cart link
        driver.find_element_by_id("nav-cart").click()
        # confirm cart is loaded and if yes delete the cart
        if driver.title.startswith("Amazon.in Shopping Cart"):
            # to delete an item from the Cart
            driver.find_element_by_xpath(
                "//div[contains(@class,'a-row sc-action-links')]//span[contains(@class,'sc-action-delete')]").click()

            time.sleep(2)
        # to confirm the item was delete successfully
        self.assertTrue(int(driver.find_element_by_id('nav-cart-count').text) < cart_count)

        # -- Post - Condition --
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
