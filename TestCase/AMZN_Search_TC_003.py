from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

"""
TC2: User should be able to add product to their cart
"""


class AddItemToCart(unittest.TestCase):
    base_url = "https://www.amazon.in"
    search_term = "How Google Tests Software"

    # -- Pre - Condition --
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/pengkedi/Documents/selenium/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # -- Steps --
    def test_amazon_home_page(self):
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

        # verify the sub cart page loaded successfully
        self.assertTrue(driver.find_element_by_id("hlb-subcart").is_enabled())
        self.assertTrue(self.driver.find_element_by_id("hlb-ptc-btn-native").is_displayed())

    # -- Post - Condition --
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
