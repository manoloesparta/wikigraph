import re
import os
import random
import requests
import concurrent.futures

WIKIPEDIA = 'https://en.wikipedia.org/'
PREFIX = '/wiki/'
DATADIR = 'data/'
cache = {}


def cleanstr(string):
    return (string.split('/')[-1])[:-1]


def visit(article):
    global cache
    url = WIKIPEDIA + PREFIX + article

    if not os.path.exists(DATADIR + article):
        print(f'Downloading {article}')
        source = str(requests.get(url).content)
        pattern = re.compile(r'\"/wiki/[a-zA-Z0-9_()-.!\']+\"')
        links = pattern.findall(source)

        res = [ cleanstr(link) for link in links ]
        final = list(dict.fromkeys(res))

        with open(DATADIR + article, 'w+') as file:
            file.write(',\n'.join(final))

        cache[article] = final
        return final
    
    try:
        res = cache[article]
        print(f'{article} in cache')
        return res

    except KeyError:
        print(f'{article} stored')

        with open(DATADIR + article, 'r') as file:
            content = file.read()
            final = content.split(',\n')

            cache[article] = final
            return final


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
        starting_points = file.read().split(',')[0:2]
        with concurrent.futures.ProcessPoolExecutor() as executor:
            [executor.submit(traverse, start) for start in starting_points]