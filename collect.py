import re
import os
import random
import requests
import concurrent.futures
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
        
        links = soup.find_all('a', attrs={ 'href': re.compile('^/wiki/[a-zA-Z0-9_()-.!\']+$') })
        res = [ link.get('href').split('/')[-1] for link in links ]
        final = list(dict.fromkeys(res))

        with open(DATADIR + article, 'w+') as file:
            file.write(',\n'.join(final))

        return final
    
    print(f'{article} downloaded')

    with open(DATADIR + article, 'r') as file:
        content = file.read()
        return content.split(',\n')

def traverse(start):
    visited = []
    queue = []
    
    queue.append(start)
    visited.append(start)

    while len(queue) > 0:
        v = queue.pop(0)
        adj = visit(v)
        
        for i in adj:
            if not i in visited:
                queue.append(i)
                visited.append(i)

if __name__ == "__main__":

    if not os.path.exists(DATADIR):
        os.mkdir(DATADIR)
        visit('Mexico')

    with open('start.csv', 'r') as file:
        starting_points = file.read().split(',')
        with concurrent.futures.ThreadPoolExecutor() as executor:
            [executor.submit(traverse, s) for s in starting_points]