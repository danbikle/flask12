
import requests

myrsp = requests.get('https://flask11.herokuapp.com')
print(myrsp.text)

import bs4
import pdb

soup = bs4.BeautifulSoup(myrsp.text, "lxml")
myh1 = soup.find('h1')
print(myh1)

'bye'
