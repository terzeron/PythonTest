#!/usr/bin/env python
#-*- coding: utf-8 -*-


import asyncio
import time


async def coroutine():
    print("in coroutine")
    time.sleep(5)
    return 'result'


event_loop = asyncio.new_event_loop()
try:
    print("starting coroutine")
    coro = coroutine()
    print("entering event loop")
    ret_value = event_loop.run_until_complete(coro)
    print("ret_value=", ret_value)
finally:
    print("closing event loop")
    event_loop.close()
