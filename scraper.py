from bs4 import BeautifulSoup
import requests
import os
import urllib.request
from requests.compat import urljoin

chasers_url = 'https://chasersjuice.com/chasers-juice-products'
response = requests.get(chasers_url)
soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')
div_tags = soup.find_all('div', {'url'})
urls = [urljoin(chasers_url, img['src']) for img in img_tags]
urls += [urljoin(chasers_url, div['style'][23:-3]) for div in div_tags]

# no dupes
urls = list(set(urls))

file = open("links.txt", "w")

for url in urls:
    try:
        print(url)
        file.write(url + '\n')
    except:
        print('failed to write url')

file.close()

for i, url in enumerate(urls):
    try:
        print(i, url)
        urllib.request.urlretrieve(url, 'images/image' + str(i) + '.jpg')
    except Exception as e:
        print('failed to download image:', e)