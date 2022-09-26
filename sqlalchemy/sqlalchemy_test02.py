#!/usr/bin/env python

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

with engine.connect() as conn:
    conn.execute(text("create table some_table (x int, y int)"))
    conn.execute(text("insert into some_table (x, y) values (:x, :y)"),
                 [{"x": 1, "y": 2}, {"x": 3, "y": 4}, {"x": 6, "y": 8}, {"x": 9, "y": 10}])
    conn.commit()

stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
with Session(engine) as session:
    result = session.execute(stmt)
    for row in result:
        print(f"x:{row.x}, y:{row.y}")

with Session(engine) as session:
    result = session.execute(text("UPDATE some_table SET y=:y WHERE x=:x"),
                             [{"x": 9, "y": 11}, {"x": 13, "y": 15}])
    session.commit()