# Web Scraping
from turtledemo.penrose import star

import requests, bs4, lxml

"""# result = requests.get('http://example.com/')
page_number = 1
final_url = base_url.format(page_number)
print(final_url)

result = requests.get(final_url)
soup = bs4.BeautifulSoup(result.text, 'lxml')
products = soup.select(".product_pod")
example = products[0]
print(example.select('.star-rating.Three'))
print(example.select('a')[1]['title'])
print(example.select('a'))
"""
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
two_star_title = []

for n in range(1, 52):
    print(n, ' out of 52', len(two_star_title), ' books found so far')
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_title.append(book_title)

for title in two_star_title:
    print(title)