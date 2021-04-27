from selenium import webdriver

driver = webdriver.Chrome("C:\\webdriver\\chromedriver.exe")
driver.get("https://www.google.com")

url = driver.current_url
print(url)
print(driver.title)