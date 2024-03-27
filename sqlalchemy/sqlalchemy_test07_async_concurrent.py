#!/usr/bin/env python


import asyncio
from sqlalchemy import Column, MetaData, select, String, Table
from sqlalchemy.ext.asyncio import create_async_engine

meta = MetaData()
t1 = Table("t1", meta, Column("name", String(50), primary_key=True))


async def async_main() -> None:
    #engine = create_async_engine("mysql+aiomysql://sqlalchemy:micro170219@localhost:3306/sqlalchemy", echo=True)
    #engine = create_async_engine("mysql+aiomysql://sqlalchemy:micro170219@localhost:3306/sqlalchemy", pool_size=10, max_overflow=20)
    engine = create_async_engine("sqlite+aiosqlite:///../sqlalchemy_test")
    size = 100000
    queries = [None] * size
    async with engine.begin() as conn:
        await conn.run_sync(meta.create_all)

        for i in range(size):
            queries[i] = conn.execute(t1.insert(), {"name": f"some name {i}"})
        result = await asyncio.gather(*queries)

    async with engine.begin() as conn:
        #result = await conn.execute(select(t1))
        #print(result.fetchall())
        await conn.execute(t1.delete())

    await engine.dispose()


asyncio.run(async_main())
