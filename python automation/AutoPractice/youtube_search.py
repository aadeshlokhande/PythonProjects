from selenium import webdriver
import time
import pyautogui as gui

driver = webdriver.Chrome()
driver.get('http://youtube.com')
time.sleep(5)
searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('BB ki vines')

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()
time.sleep(5)

bb = driver.find_element_by_class_name('style-scope ytd-channel-renderer')
bb.click()
time.sleep(5)
gui.press('f')
