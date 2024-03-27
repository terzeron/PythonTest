#!/usr/bin/env python


import asyncio
from sqlalchemy import Column, MetaData, String, Table, select
from sqlalchemy.ext.asyncio import create_async_engine

meta = MetaData()
t1 = Table("t1", meta, Column("name", String(50), primary_key=True))


async def async_main() -> None:
    # engine = create_async_engine("mysql+aiomysql://sqlalchemy:micro170219@localhost:3306/sqlalchemy", echo=True, )
    # engine = create_async_engine("mysql+aiomysql://sqlalchemy:micro170219@localhost:3306/sqlalchemy", pool_size=10, max_overflow=20)
    engine = create_async_engine("sqlite+aiosqlite:///../sqlalchemy_test")
    size = 100000

    async with engine.begin() as conn:
        await conn.run_sync(meta.create_all)

        for i in range(size):
            await conn.execute(t1.insert(), {"name": f"some name {i}"})

    async with engine.begin() as conn:
        # result = await conn.execute(select(t1).where(t1.c.name == "some name 1"))
        # print(result.fetchall())
        await conn.execute(t1.delete())

    await engine.dispose()


asyncio.run(async_main())
