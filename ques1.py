import requests
from bs4 import BeautifulSoup
url = input("enter url of site:")
r = requests.get(url)
c = r.content
soup = BeautifulSoup(c,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))
