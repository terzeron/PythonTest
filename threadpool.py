#!/usr/bin/env python3

import timeit
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen

urls = ['https://google.com', 'https://apple.com', 'http://terzeron.net']

def fetch(url):
    print('start', url)
    urlopen(url)
    print('end', url)

start = timeit.default_timer()

with ThreadPoolExecutor(max_workers=5) as executor:
    for url in urls:
        executor.submit(fetch, url)

duration = timeit.default_timer() - start
print(duration)
