#print out list of all articles on NY Times homepage
from bs4 import BeautifulSoup
import requests



#title = soup.find('span', 'articletitle').string

def print_title(url = "https://www.nytimes.com/"):
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, 'lxml')
    for title in soup.find_all('span'):
        print("\n", title)
    #list = []
    #for link in soup.find_all('title'):
     #   list.append(link.string)
    
    #print("\n", list)
    
print_title()