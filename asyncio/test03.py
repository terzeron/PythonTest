#!/usr/bin/env python

import sys
import asyncio


async def my_coroutine(task_name, seconds_to_sleep=3):
    print("%s sleeping for %d seconds" % (task_name, seconds_to_sleep))
    await asyncio.sleep(seconds_to_sleep)
    print("%s is finished" % (task_name))


async def main():
    tasks = [
        my_coroutine('task1', 4),
        my_coroutine('task2', 3),
        my_coroutine('task3', 2)]
    for task in tasks:
        #print(task)
        await asyncio.create_task(task)
        #await task


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
