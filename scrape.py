# practicing to scrape the web
import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

# picking our site
response = requests.get(url)

# picking our parser
soup = BeautifulSoup(response.text, 'lxml')

# getting the span tags only
quotes = soup.find_all('span', class_='text')

# getting all the authors as well
authors = soup.find_all('small', class_='author')

# getting the tag for quotes
tags = soup.find_all('div', class_='tags')

# now printing the authors and quotes
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quote_tags = tags[i].find_all('a', class_='tag')
    for quote_tag in quote_tags:
        print(quote_tag.text)
