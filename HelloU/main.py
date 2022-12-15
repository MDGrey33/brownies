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
# for item in soup.select('.toctext'):
    # print(item.text)
# print(soup.select('.toctext')[i])
# print(text)

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text, 'lxml')
images = soup.select('.thumbimage')[0]
print(images['src'])
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png')
print(image_link.content)
f = open('my_computer_image.png', 'wb')
f.write(image_link.content)
f.close()
