"""
AGENDA

Basic webdriver Commands
capture title of the page
capture URL of the page
closing & quitting browsers
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
driver = webdriver.Chrome('/home/aadesh/Documents/PycharmProjects/chromedriver/chromedriver')
driver.get('https://www.geeksforgeeks.org/')


print(driver.title)                 # print title the page

print(driver.current_url)           # print current URL

driver.find_element_by_xpath("//*[@id='hslider']/li[7]/a").click()      #click button with xPath

time.sleep(5)

# driver.close()                      # only one tab will close - currently focused browser

driver.quit()                       #Chrome will close