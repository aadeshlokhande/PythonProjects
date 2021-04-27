import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def Spy(Domain,Word):

    url = Domain
    word = Word
    mainList = []
    urls = []

    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    for link in soup.find_all('a'):
        urls.append(str(link.get('href')).replace("#",url))

    for i in urls:
        if "http" in i:
            mainList.append(i)

    for suburl in mainList:
        file = open("URLS.txt", "a")
        file.write(f"{suburl} \n")
        file.close()

    for i in mainList:
        try:
            driver = webdriver.Chrome('/home/aadesh/Documents/Cd/chromedriver')
            driver.get(i)
            # driver.implicitly_wait(10)
            string = str(driver.page_source).lower()
            data = i+" :: "+str(string.count(word))

            file = open("Data.txt", "a")
            file.write(f"{data} \n")
            file.close()

            print(data)

            driver.quit()
            time.sleep(2)
        except:
            print("Didn't open : ",i)
