from bs4 import BeautifulSoup as bs
import requests as req

URL = 'https://apache.worketix.com/(S(v2d2ycahhdish0jwuez0swj1))/entrance/default.aspx'
page = req.get(URL)

soup = bs(page.content, 'html.parser')

with open('test.txt', 'w') as f:
    f.write(soup.prettify())