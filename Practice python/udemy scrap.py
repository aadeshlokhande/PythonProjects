# importing the libraries
from bs4 import BeautifulSoup
import requests

url="https://www.udemy.com/course/learn-economics-from-scratch-eco04/"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
print(soup.prettify()) # print the parsed data of html