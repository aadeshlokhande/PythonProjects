from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/home/aadesh/Documents/Cd/chromedriver')
driver.get('https://cyberscopesolution.in/')


string = str(driver.page_source).lower()
word = "team"
print(string.count(word))

driver.quit()