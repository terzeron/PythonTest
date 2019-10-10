#!/usr/bin/env python3

import asyncio
import timeit

start = timeit.default_timer()

async def compute(x, y):
    print("Compute %s + %s" % (x, y))
    duration = timeit.default_timer() - start
    print("1", duration)
    await asyncio.sleep(1.0)
    duration = timeit.default_timer() - start
    print("2", duration)
    return x + y

async def print_sum(x, y):
    duration = timeit.default_timer() - start
    print("3", duration)
    result = await compute(x, y)
    duration = timeit.default_timer() - start
    print("4", duration)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
duration = timeit.default_timer() - start
print("5", duration)
loop.run_until_complete(print_sum(1, 2))
duration = timeit.default_timer() - start
print("6", duration)
loop.close()
duration = timeit.default_timer() - start
print("7", duration)
