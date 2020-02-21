# practicing to scrape multiple pages on the web
import requests
from bs4 import BeautifulSoup

# picking our site
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
# getting the response
response = requests.get(url)
# picking our parser
soup = BeautifulSoup(response.text, 'lxml')

items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1
for i in items:
    item_name = i.find('h4', class_='card-title').text.strip('\n')
    item_price = i.find('h5').text
    print('%s ) Price: %s, Item Name: %s' % (count, item_price, item_name))
    count = count + 1