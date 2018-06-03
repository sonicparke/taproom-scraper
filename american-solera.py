from requests import get
from bs4 import BeautifulSoup

url = "https://americansolera.com/current-selection/current-drafts/"

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
pTag = html_soup.find_all('p')
extracted_records = []
taproom = ''
last_taproom = 'none'
beer = ''

for tag in pTag:
  spanTag = tag.find('span')
  if spanTag:
    strongTag = spanTag.find('strong')
    if strongTag:
      taproom = strongTag.text.strip()
      extracted_records = {
        'location': taproom
      }
      print('taproom: ', taproom)

  print('tag: ', tag)
  if last_taproom != taproom:
    last_taproom = taproom
    # while last_taproom == taproom:
    print('last_taproom: ', last_taproom)
    print('tag: ', tag)
    # Filter out Headers
    if tag.find('strong'):
      tag.extract()

    # else:
    #   left_column = tag.parent.parent.parent.parent.find_all('div', class_='vc_col-has-fill')

    #   for div in left_column:

    #     found_beer = [x for x in div.div.div.div.div if x.name == 'p']

    #     # beer = found_beer[0].text.strip()
    #     print('found_beer: ', found_beer)

    #   beers = {
    #     'beer_name': beer
    #   }
      # print('BEER: ', beer)


print('done')
