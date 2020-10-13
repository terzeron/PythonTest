#!/usr/bin/env python


def fib(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

for x in fib(10):
    print(x)
