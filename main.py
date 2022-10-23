from requests import get
import random

levels = ['g4','g3','g2','g1']
random.shuffle(levels)
dps =['g4', 'g3', 'g2', 'g1']
random.shuffle(dps)
for level in levels:
    URL = f'https://solved.ac/search?query=*{level}!%40zszszszs%20s%23200..%20%2FICPC'
    if(level == dps[0] or level == dps[1]):
        URL += '%20%23dp%20'
    URL += '&sort=random&direction=asc&page=1'
    res = get(URL)
    cont = str(res.content)
    idx = cont.index('problemId') + 11
    start = idx
    while cont[idx] != ',':
        idx += 1
    print(f'https://noj.am/{cont[start:idx]}')