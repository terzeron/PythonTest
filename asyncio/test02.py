#!/usr/bin/env python


import asyncio


async def my_coroutine(future, task_name, seconds_to_sleep=3):
    print("%s sleeping for %d seconds" % (task_name, seconds_to_sleep))
    asyncio.sleep(seconds_to_sleep)
    future.set_result("%s is finished" % (task_name))


def got_result(future):
    print(future.result())


loop = asyncio.get_event_loop()
future1 = asyncio.Future()
future2 = asyncio.Future()

tasks = [
    my_coroutine(future1, 'task1', 3),
    my_coroutine(future2, 'task2', 1)]
future1.add_done_callback(got_result)
future2.add_done_callback(got_result)

loop.run_until_complete(asyncio.wait(tasks))
loop.close()
