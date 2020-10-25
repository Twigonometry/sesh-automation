import requests
from bs4 import BeautifulSoup as bs

sesh_get = requests.get("https://www.shefesh.com")

#get soup
soup = bs(sesh_get.text, 'html.parser')

#get h3 elements
print("Headers:")
headers = soup.find_all('h3')
for h in headers:
    print("Header text: " + h.get_text())

#get img sources
print("\nImages:")
images = soup.find_all('img')
for i in images:
    print("Image source: " + i['src'])

#get script sources
print("\nScripts:")
scripts = soup.find_all('script')
for s in scripts:
    print("Script source: " + s['src'])