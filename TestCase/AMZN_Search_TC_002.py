from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_url = "https://www.amazon.in"

search_term = "How Google Tests Software"

# -- Pre_Condition -- 
# declare and initialze driver variable
driver = webdriver.Chrome(executable_path="/Users/pengkedi/Documents/selenium/chromedriver")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(base_url)
assert "Amazon" in driver.title

# --Steps --
# locate search textbox
searchTextBox = driver.find_element_by_id("twotabsearchtextbox")
searchTextBox.clear()
searchTextBox.send_keys(search_term)
searchTextBox.send_keys(Keys.RETURN)
print(driver.title)

assert "Amazon.in: {}".format(search_term) in driver.title
assert "No results found." not in driver.page_source

# --Post - Condition --
driver.close() 