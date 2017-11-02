#!/usr/bin/env python
import time


def generator_function():
    for i in range(3):
        yield i

gen = generator_function()
print(next(gen))
time.sleep(1)
print(next(gen))
time.sleep(1)
print(next(gen))
time.sleep(1)
print(next(gen))
time.sleep(1)
