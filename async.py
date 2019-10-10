#!/usr/bin/env python3

import asyncio
import timeit

async def hello_world():
    print("hello world!")

start = timeit.default_timer()

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
loop.close()

duration = timeit.default_timer() - start
print(duration)
