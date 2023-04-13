#!/usr/bin/env python

import asyncio


async def main():
    result = await asyncio.sleep(3, result='hello')
    print(result)


asyncio.run(main())
