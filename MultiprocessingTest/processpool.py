#!/usr/bin/env python

import timeit
from concurrent.futures import ProcessPoolExecutor
from urllib.request import urlopen

urls = ['https://google.com', 'https://apple.com', 'http://terzeron.net']

def fetch(url):
    print('start', url)
    urlopen(url)
    print('end', url)

start = timeit.default_timer()

with ProcessPoolExecutor(max_workers=5) as executor:
    for url in urls:
        executor.submit(fetch, url)

duration = timeit.default_timer() - start
print(duration)
