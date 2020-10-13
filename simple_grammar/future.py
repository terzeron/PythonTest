#!/usr/bin/env python

from concurrent import futures

def big_calculation(num):
    return num ** 10

arguments = list(range(20))


with futures.ProcessPoolExecutor() as executor:
    result = list(executor.map(big_calculation, arguments))
    print(result)

'''
def test_func(num):
    print("test_func(%d)" % (num))
    return num*2
    
result = list(map(test_func, arguments))
print(result)
'''
