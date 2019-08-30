import requests
from bs4 import BeautifulSoup
r = requests.get("http://bioguide.congress.gov/biosearch/biosearch1.asp")
c = r.content
soup = BeautifulSoup(c,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))
	