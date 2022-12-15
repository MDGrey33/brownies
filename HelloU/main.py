# Web Scraping
import requests, bs4, lxml

result = requests.get('http://example.com/')
# print(result.text)
soup = bs4.BeautifulSoup(result.text, 'lxml')
# element = soup.select('title')
# element = soup.select('h1')
element = soup.select('title')[0].get_text()
site_paragraphs = soup.select("p")
# print(site_paragraphs[0].getText())

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')
for item in soup.select('.toctext'):
    print(item.text)
# print(soup.select('.toctext')[i])
# print(text)
