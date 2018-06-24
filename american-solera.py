from requests import get
from bs4 import BeautifulSoup

url = "https://americansolera.com/current-selection/current-drafts/"

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
pTag = html_soup.find_all('p')
extracted_records = []
location1 = []
location2 = []
taproom = ''
last_taproom = 'none'
beer = ''

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
            if not location1:
                location1.append(taproom)
                # print('location1: ', location1)

            else:
                location2.append(taproom)
                # print('location2: ', location2)

    # If there is a <strong> tag but not inside a <span> then it's probably a column heading
    strongTag = tag.find('strong')
    if strongTag:
        parent = strongTag.find_parent('p')
        parent.decompose()

    # Grab the beers and descriptions
    else:
        if not location1 or not location2:
            location1.append(tag.text.strip())
        else:
            location2.append(tag.text.strip())


print('location1: ', location1)
print('location2: ', location2)

# print('extracted_records: ', extracted_records)
print('done')
