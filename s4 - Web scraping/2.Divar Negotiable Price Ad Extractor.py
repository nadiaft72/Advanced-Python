# Extract and Print Negotiable Price Ads from Divar:
# This program extracts and prints ads with a "توافقی" (Negotiable) price tag from the first page of the Divar website (https://divar.ir/s/tehran).
# It uses the requests library to fetch the page's HTML content and the BeautifulSoup library to parse the HTML and navigate the elements.
# The ads with the desired "توافقی" price tag are then printed in the output.

import requests
from bs4 import BeautifulSoup

# Fetch the HTML content of the first page of the Divar website for Tehran.
res = requests.get('https://divar.ir/s/tehran')

# Parse the HTML content using BeautifulSoup.
soup = BeautifulSoup(res.text, 'html.parser')

# Find all the elements with the class "kt-post-card__body," which represent the ads on the page.
res = soup.find_all("div", attrs={"class": "kt-post-card__body"})

# Loop through each ad and extract the title and description.
# If the description contains "توافقی" (Negotiable), print the ad's title.
for car in res:
    x = car.find("div", attrs={"class": "kt-post-card__title"})
    t = car.find("div", attrs={"class": "kt-post-card__description"})
    if t != None and t.text == "توافقی":
        print(x.text)
