# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:45:32 2020

@author: Bryce
"""
from bs4 import BeautifulSoup
import requests

base_url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features="lxml")

for article_text in soup.find_all("div", class_="content-background"):
    if article_text.p:
        print(article_text.text.replace("\n", " ").strip())
    else:
        print(article_text.contents[0].strip())
 
    
