import re
import requests
import os
from bs4 import BeautifulSoup

WIKIPEDIA = 'https://en.wikipedia.org/'
PREFIX = '/wiki/'
DATADIR = 'data/'

def get_neighbors(article):
    url = WIKIPEDIA + PREFIX + article
    if not os.path.exists(DATADIR + article):        
        source = requests.get(url)
        soup = BeautifulSoup(source.content, 'lxml')
        
        links = soup.find_all('a', attrs={ 'href': re.compile('^/wiki/[a-zA-Z0-9]+$') })
        res = [ link.get('href').split('/')[-1] for link in links ]
        
        with open(DATADIR + article, 'w+') as f:
            f.write(',\n'.join(res))

    print(article + ' Already exist')        
        

if __name__ == "__main__":

    if not os.path.exists(DATADIR):
        os.mkdir(DATADIR)
        
    res = get_neighbors('Mexico')