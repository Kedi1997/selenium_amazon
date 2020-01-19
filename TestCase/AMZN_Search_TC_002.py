from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

"""
TC2: User should be able to search products
"""


class AmazonSearch(unittest.TestCase):
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

        self.assertIn(self.assertIn(), driver.title)
        self.assertNotIn("No results found.", self.driver.page_source)

    # -- Post - Condition --
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
