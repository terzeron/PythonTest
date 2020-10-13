#!/usr/bin/env python

import threading

def worker(data):
    try:
        print(data.value)
        data.value += 1
        print(data.value)
    except AttributeError:
        print("no value")


local_data = threading.local()
local_data.value = 10

for i in range(10):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()
    
