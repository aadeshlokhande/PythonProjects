from selenium import webdriver
import time

driver = webdriver.Chrome()

web = driver.get('www.google.com')
time.sleep(5)