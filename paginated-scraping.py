import requests
from bs4 import BeautifulSoup as bs

base_url = "https://www.shefesh.com"

sesh_get = requests.get(base_url)

#get soup
soup = bs(sesh_get.text, 'html.parser')

#get all anchor tags
anchors = soup.find_all('a')

#for each link, print and offer chance to scrape next page
for a in anchors:
    href = a['href']
    print(str(href))
    go_deeper = input("Want to go deeper? Y/anything else\n").upper()

    #scrape next page?
    if go_deeper == "Y" or go_deeper == "YES":
        #append base_url to start if it's a relative URL
        if href[0] == "/":
            href = base_url + href

        new_get = requests.get(href)
        new_soup = bs(new_get.text, 'html.parser')

        print("URLs under " + href)

        #find more anchor tags
        new_as = new_soup.find_all('a')
        for n in new_as:
            print("\t" + str(n['href']))