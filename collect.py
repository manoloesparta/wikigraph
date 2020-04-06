import re
import os
import requests
import concurrent.futures

WIKIPEDIA = 'https://en.wikipedia.org/'
PREFIX = '/wiki/'
DATADIR = 'data/'

def cleanstr(string):
    return (string.split('/')[-1])[:-1]

def visit(article):
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

        return final

    with open(DATADIR + article, 'r') as file:
        content = file.read()
        return content.split(',\n')

def traverse(start):
    visited = os.listdir(DATADIR)
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
        with concurrent.futures.ProcessPoolExecutor() as executor:
            [ executor.submit(traverse, start) for start in starting_points ]