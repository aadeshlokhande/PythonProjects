import bs4
import requests

url  = "https://www.mycodingzone.net/blog/english"
data = requests.get(url)

soup = bs4.BeautifulSoup(data.text, "html.parser")
# print(soup.prettify())                          # Print all html text beautifully

# for para in soup.find('p'):                         # find function find 1st data from html data
    # print(para)

# for para in soup.find_all('p'):                     # find_all function find all data from html data
#     print(para.text)                                # we use text from removing tags and print only text
    


