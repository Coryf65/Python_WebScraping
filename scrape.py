# practicing to scrape the web
import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

print(soup)