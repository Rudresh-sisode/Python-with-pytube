import requests
from bs4 import BeautifulSoup

r = requests.get("file:///C:/Users/Documents/Documents/page.html")
c = r.content
soup = BeautifulSoup(c,"html.parser")
print(soup.prettify())

