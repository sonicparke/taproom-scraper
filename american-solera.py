from requests import get
from bs4 import BeautifulSoup

url = "https://americansolera.com/current-selection/current-drafts/"

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
pTag = html_soup.find_all('p')
extracted_records = []
taproom = ''
last_taproom = ''
beer = ''
section = dict({})
section_list = dict({})



def getTaproom(pTag):
  for tag in pTag:
  # print(tag)


    # Get Taproom Locations
    spanTag = tag.find_all('span')
    if spanTag:
      for span in spanTag:
        locations = span.find_all('strong')
        for location in locations:
          if location:
            print(location)
            # taproom = location.text.strip()
            return location.text.strip()
            # extracted_records = {
            #   'location': location.text.strip()
            # }


  # else:
  #   if last_taproom != taproom:
  #     last_taproom = taproom
  #     print(taproom)
  #
  #     section['location'] = taproom
  #
  #
  #
  #     beers = []
  #     section_list['beers'] = {}
  #     # Get Beer Names
  #     left_column = html_soup.find_all('div', class_='vc_col-has-fill')
  #     for div in left_column:
  #       title = div.find_all('div', class_='wpb_content_element')
  #       found_beer = [x for x in div.div.div.div.div if x.name == 'p']
  #       beer = found_beer[0].text.strip()
  #       beers = {
  #         'beer_name': beer
  #       }
  #       # print(section)
  #       # extracted_records[taproom].append(record)
  #       # extracted_records.index(taproom).append(record)
  #       # print('================')
  #       # print(taproom)
  #       # print(beer)
  #       # print('================')
  #
  #     # section_list['beers'].append(beers)
  # # section
  # # extracted_records.append(section_list)
  # extracted_records.append(section)

print(getTaproom(pTag))



