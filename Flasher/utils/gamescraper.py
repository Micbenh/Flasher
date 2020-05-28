import requests
from bs4 import BeautifulSoup as bs
import sys

def get_links():
    url = sys.argv[1]
    page = requests.get(url).text
    soup = bs(page, 'html.parser')

    with open('gamelinks.txt','a') as gl:
        for link in soup.find_all('a'):
            links = link.get('href')
            gl.write(links + "\n")

if __name__ == '__main__':
    get_links()

    