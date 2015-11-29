# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

html = requests.get('http://www.tantengvip.com')

html = BeautifulSoup(html.content,'lxml')

list = html.find_all('article')

for article in list:
    print article.contents[1]