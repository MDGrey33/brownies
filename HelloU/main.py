# H20 Wave ui
# pip install h2o_wave
# download wave server https://wave.h2o.ai/docs/installation and unpacks
# in terminal go to wave directory and ./waved to start the server
from h2o_wave import site, ui
import time

name = 'Roland'

main = site['/']

main['title'] = ui.markdown_card(
    box='1 1 2 2',
    title=f'Hello {name}',
    content='This is the main page body'
)

main['body'] = ui.markdown_card(
    box='3 1 2 2',
    title=f'{name} What are you up tp today?',
    content='Lets put allot of text here to see how this looks like. \nWhat if we make two lines, would this still work?'
)


main.save()


page = site['/beer']

beer_verse = '''={{before}} bottles of beer on the wall, {{before}} bottles of beer.

Take one down, pass it around, {{after}} bottles of beer on the wall...
'''

beer_card = page.add('wall', ui.markdown_card(
    box='1 1 4 2',
    title='99 Bottles of Beer',
    content=beer_verse,
    data=dict(before='99', after='98'),
))

for i in range(99, 0, -1):
    beer_card.data.before = str(i)
    beer_card.data.after = str(i - 1)
    page.save()
    time.sleep(1)
