# Web Scraping
import requests, bs4, lxml

author_list = []
quote_list = []
tag_list = []

for n in range(1, 100):
    print('Scraping page ', n)
    base_url = 'http://quotes.toscrape.com/page/{}/'
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Extract authors
    authors = soup.select('.author')
    for author in authors:
        author_list.append(author.text)

    # Extract Quotes
    quotes = soup.select('.text')
    for quote in quotes:
        quote_list.append(quote.text)

    # Extract tags
    tags_box = soup.select('.col-md-4.tags-box')
    tags = tags_box[0].select('a')
    for tag in tags:
        tag_list.append(tag.text)

    pager = soup.select('.pager')
    next_page = pager[0].select('.next')
    if len(next_page) == 0:
        print(n, ' pages scraped.')
        print(len(set(author_list)), ' authors collected')
        print(len(quote_list), ' quotes collected')
        break


print(quote_list)
print(set(author_list))
print(set(tag_list))

# tag = tags_box.select('a')[1]['href']
# print(tag)

# On page 1
# Capture the page
# Get Authors names {} (<small class="author" itemprop="author">Albert Einstein</small>)
# Get Quotes (<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>)
# get top 10 tags (<a class="tag" style="font-size: 26px" href="/tag/life/">life</a>)
# <div class="col-md-4 tags-box">
#
#             <h2>Top Ten tags</h2>
#
#             <span class="tag-item">
#             <a class="tag" style="font-size: 28px" href="/tag/love/">love</a>
#             </span>
#     </div>
# Loop pages till the end
# No next button causes a stop
# <ul class="pager">
#             <li class="next">
#                 <a href="/tag/inspirational/page/2/">Next <span aria-hidden="true">→</span></a>
#             </li>
#         </ul>
