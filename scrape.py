# practicing to scrape the web
import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

# picking our site
response = requests.get(url)

# picking our parser
soup = BeautifulSoup(response.text, 'lxml')

# seeing the html
print(soup)