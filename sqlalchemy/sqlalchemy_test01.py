#!/usr/bin/env python

from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

with engine.connect() as conn:
    conn.execute(text("create table some_table (x int, y int)"))
    conn.execute(text("insert into some_table (x, y) values (:x, :y)"),
                 [{"x": 1, "y": 2}, {"x": 3, "y": 4}])
    conn.commit()

with engine.begin() as conn:
    conn.execute(text("insert into some_table (x, y) values(:x, :y)"),
                 [{"x": 6, "y": 8}, {"x": 9, "y": 10}])

with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result:
        print(f"x:{row.x}, y:{row.y}")
        print(row[0], row[1])

with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for x, y in result:
        print(x, y)

with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for dict_row in result.mappings():
        x = dict_row['x']
        y = dict_row['y']
        print(x, y)

with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table WHERE y > :y"),
                          {"y": 2})
    for row in result:
        print(f"x:{row.x}, y:{row.y}")
    result = conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
                          {"x": 11, "y": 12}, {"x": 13, "y": 14})
    conn.commit()

stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
with engine.connect() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(f"x:{row.x}, y:{row.y}")
