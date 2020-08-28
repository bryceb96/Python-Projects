# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 20:56:19 2020

@author: Bryce
"""

#program will read in the article titles from the New York Times to the Lesson21.doc file and then print out the Lesson21.doc file
from bs4 import BeautifulSoup
import requests



#title = soup.find('span', 'articletitle').string

def print_title(url = "https://www.nytimes.com/"):
    with open('C:/Users/Bryce/Dropbox/Documents/Kent State/Python lessons/Lesson21/Lesson21doc.txt', 'wt', encoding = 'utf-8') as fin:
        r = requests.get(url)
        r_html = r.text
        soup = BeautifulSoup(r_html, 'lxml')
        for title in soup.find_all("span"):
            fin.write(str(title))
            #else:
                #print(title.contents[0].strip())
    #list = []
    #for link in soup.find_all('title'):
     #   list.append(link.string)
    with open('C:/Users/Bryce/Dropbox/Documents/Kent State/Python lessons/Lesson21/Lesson21doc.txt', 'rt', encoding = 'utf-8') as fout:
        [print("\n", line) for line in fout]
    
print_title()

