import re
import requests
import os
from bs4 import BeautifulSoup

WIKIPEDIA = 'https://en.wikipedia.org/'
PREFIX = '/wiki/'
DATADIR = 'data/'


def visit(article):
    url = WIKIPEDIA + PREFIX + article

    if not os.path.exists(DATADIR + article):
        print(f'Downloading {article}')

        source = requests.get(url)
        soup = BeautifulSoup(source.content, 'lxml')
        
        links = soup.find_all('a', attrs={ 'href': re.compile('^/wiki/[a-zA-Z0-9]+$') })
        res = [ link.get('href').split('/')[-1] for link in links ]
        final = list(dict.fromkeys(res))
        
        with open(DATADIR + article, 'w+') as file:
            file.write(',\n'.join(final))

        return final
    
    print(f'{article} downloaded')        

    with open(DATADIR + article, 'r') as file:
        content = file.read()
        return content.split(',\n')

if __name__ == "__main__":

    if not os.path.exists(DATADIR):
        os.mkdir(DATADIR)
        
    res = visit('Mexico')
    for i in res:
        for j in visit(i):
            visit(j)
