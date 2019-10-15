#!/usr/bin/env python

def sqr(nums):
    result = []
    for i in nums:
        yield i*i

nums = sqr([1, 2, 3, 4, 5])

for num in nums:
    print(num)
