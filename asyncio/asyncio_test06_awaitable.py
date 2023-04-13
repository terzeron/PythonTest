#!/usr/bin/env python

import asyncio


async def nested():
    print("nested()")
    return 42


async def execute_coroutine():
    print("execute_coroutine()")
    #nested()  # not executed
    print(await nested())


async def execute_task():
    print("execute_task()")
    task = asyncio.create_task(nested())
    await task


async def function_that_returns_future():
    print("function_that_returns_future()")
    future = asyncio.Future()
    # returns a future that is either pending, done or cancelled
    #future.set_result(nested)
    #future.cancel()
    return future

async def coroutine():
    print("coroutine()")
    return 100

async def main():
    print("main()")

    await execute_coroutine()

    await execute_task()

    future = await function_that_returns_future()
    print(future)

    # execute awaitables concurrently
    await asyncio.gather(function_that_returns_future(), coroutine())


asyncio.run(main())
