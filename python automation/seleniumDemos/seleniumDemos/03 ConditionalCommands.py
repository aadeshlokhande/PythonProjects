"""
AGENDA
- is_displayed()
- is_enabled()
- is_selected()
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/home/aadesh/Documents/Cd/chromedriver')
driver.get('https://www.youtube.com/')

user_ele = driver.find_element_by_name('search_query')
print(user_ele.is_displayed())
print(user_ele.is_enabled())

user_ele.send_keys("bb ki vines")
driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
