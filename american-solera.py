from requests import get
from bs4 import BeautifulSoup
import re

url = "https://americansolera.com/current-selection/current-drafts/"

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
pTag = html_soup.find_all('p')
locations = []
location1List = []
location2List = []
location1obj = {
    "taproom": "",
    "on_tap": []
}
location2obj = {
    "taproom": "",
    "on_tap": []
}
location1beers = []
location2beers = []

# Remove search text at end of page
search_text = html_soup.findAll("p", class_="search-text")
for search in search_text:
    search.decompose()

# Look at all the <p> tags
for tag in pTag:

    # If there is a span it's probably a taproom location
    spanTag = tag.find('span')
    if spanTag:
        strongTag = spanTag.find('strong')
        if strongTag:
            taproom = strongTag.text.strip()
            if not location1List:
                location1List.append(taproom)

            else:
                location2List.append(taproom)

    # If there is a <strong> tag but not inside a <span> then it's probably a column heading
    strongTag = tag.find('strong')
    if strongTag:
        parent = strongTag.find_parent('p')
        parent.decompose()

    # Grab the beers and descriptions
    else:
        text = tag.text.strip()
        if text != '':
            # check for rouge &nbsp; that comes through as \xa0
            if '\xa0' in text:
                text = re.sub(u'\xa0', u' ', text)

            if not location1List or not location2List:
                location1List.append(text)
            else:
                location2List.append(text)


# Build the objects
location1obj['taproom'] = location1List.pop(0)
location2obj['taproom'] = location2List.pop(0)

while location1List:
    location1beers = {
        "beer": location1List.pop(0),
        "description": location1List.pop(0)
    }
    location1obj['on_tap'].append(location1beers)

while location2List:
    location2beers = {
        "beer": location2List.pop(0),
        "description": location2List.pop(0)
    }
    location2obj['on_tap'].append(location2beers)

locations.append(location1obj)
locations.append(location2obj)

print('locations: ', locations)
print('done')
