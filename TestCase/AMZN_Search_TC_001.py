from selenium import webdriver
import unittest

"""
TC1: User should be able to load Amazon's Home Page
"""


class AmazonHomePage(unittest.TestCase):
    base_url = "https://www.amazon.in"

    # -- Pre - Condition --
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/pengkedi/Documents/selenium/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # -- Steps --
    def test_load_home_page(self):
        driver = self.driver
        driver.get(self.base_url)
        self.assertIn("Amazon", driver.title)

    # -- Post - Condition --
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
