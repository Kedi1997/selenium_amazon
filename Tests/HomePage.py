from selenium import webdriver

from Resources.Locators import Locators
from Tests.BasePage import BasePage
from Tests.TestData import TestData


class HomePage(BasePage):
    """ Home page of Amazon """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def search(self):
        self.driver.find_element(*Locators.SEARCH_TEXTBOX).clear()
        self.enter_text(Locators.SEARCH_TEXTBOX, TestData.SEARCH_TERM)
        self.click(Locators.SEARCH_SUBMIT_BUTTON)


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="/Users/pengkedi/Documents/selenium/chromedriver")
    home_page = HomePage(driver)
    home_page.search()
