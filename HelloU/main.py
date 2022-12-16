# Web Scraping
import requests, bs4, lxml

author_list = set()
quote_list = []
tag_list = set()

for n in range(1, 100):
    print('Scraping page ', n)
    base_url = 'http://quotes.toscrape.com/page/{}/'
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Extract authors
    authors = soup.select('.author')
    for author in authors:
        author_list.add(author.text)

    # Extract Quotes
    quotes = soup.select('.text')
    for quote in quotes:
        quote_list.append(quote.text)

    # Extract tags
    tags_box = soup.select('.col-md-4.tags-box')
    tags = tags_box[0].select('a')
    for tag in tags:
        tag_list.add(tag.text)

    pager = soup.select('.pager')
    next_page = pager[0].select('.next')
    if len(next_page) == 0:
        print(n, ' pages scraped.')
        print(len(author_list), ' authors collected')
        print(len(quote_list), ' quotes collected')
        break


print(quote_list)
print(author_list)
print(tag_list)