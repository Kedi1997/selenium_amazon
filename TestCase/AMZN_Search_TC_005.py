import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

"""
TC5: User must sign in to checkout
"""


class SignInCheckOut(unittest.TestCase):
    base_url = "https://www.amazon.in"
    search_term = "How Google Works"

    # -- Pre - Condition --
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/pengkedi/Documents/selenium/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # -- Steps for AMZN_Search_TC_005 --
    def test_AMZN_Search_TC_005_test_signin_to_checkout(self):
        """User must sign in to checkout"""
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
        driver.find_element_by_id('hlb-ptc-btn-native').click()

        self.assertTrue(driver.title.startswith("Amazon Sign In"))
        self.assertTrue(driver.find_element_by_id('ap_email').is_displayed())

    # -- Post - Condition --
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
