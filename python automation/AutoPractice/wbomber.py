# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
#
# driver.get('https://web.whatsapp.com/')
#
# name = input('Enter Contact name = ')
# message = input('Enter your massege = ')
# count = int(input('Enter the count of massege = '))
#
# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
# user.click()
#
# text_box = driver.find_element_by_class_name('_3u328')
#
# for i in range(count):
#     text_box.send_keys(message)
#     driver.find_element_by_class_name('_3M-N-').click()
#     time.sleep(1)






import pywhatkit
pywhatkit.sendwhatmsg("+918857819957","bhula",3,14)


