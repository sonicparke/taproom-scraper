from requests import get
from bs4 import BeautifulSoup

url = "https://www.heirloomrusticales.com/beers-on-tap/"

response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
beers = html_soup.find_all('h2', class_='text-align-center')

extracted_records = []
for beer in beers:
  if not beer.text.isspace() and not beer.find_previous_sibling('h3'):
    record = {
      'beer_name': beer.text,
      # 'description': beer.find_next_sibling('p').text
    }

    extracted_records.append(record)
print(extracted_records)
