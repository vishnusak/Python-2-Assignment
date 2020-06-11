# Use the BeautifulSoup and requests Python packages to print out a list of all the article 
# titles on the New York Times homepage.(https://www.nytimes.com/)

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.nytimes.com"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

headlines = []
for link in soup.findAll('h2'):
    if link.text.strip():
        headlines.append(link.text)
headlines.sort()

for l in headlines:
    print("--- {} ---".format(l))