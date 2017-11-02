#!/usr/bin/env python

def fib():
    a, b = 0, 1
    while a < 1000:
        yield a
        a, b = b, a+b

for i in fib():
    print(i)