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
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
for i in items:
    item_name = i.find('h4', class_='card-title').text.strip('\n')
    item_price = i.find('h5').text
    print('%s ) Price: %s, Item Name: %s' % (count, item_price, item_name))
    count = count + 1

pages = soup.find('ul', class_='pagination')

urls = []
# getting all the links
links = pages.find_all('a', class_='page-link')

# try to convert to int
for link in links:
    page_num = int(link.text) if link.text.isdigit() else None
    if page_num != None:
        x = link.get('href')
        urls.append(x)

# See all items on page 1
print(urls)
count = 1

for i in urls:
    new_url = url + i
    response = requests.get(new_url)
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        item_name = i.find('h4', class_='card-title').text.strip('\n')
        item_price = i.find('h5').text
        print('%s ) Price: %s, Item Name: %s' % (count, item_price, item_name))
        count = count + 1



