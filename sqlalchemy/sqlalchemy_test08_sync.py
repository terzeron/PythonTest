#!/usr/bin/env python


from sqlalchemy import Column, MetaData, select, String, Table, create_engine

meta = MetaData()
t1 = Table("t1", meta, Column("name", String(50), primary_key=True))


def main() -> None:
    #engine = create_engine("mysql://sqlalchemy:micro170219@localhost:3306/sqlalchemy", echo=True)
    #engine = create_engine("mysql://sqlalchemy:micro170219@localhost:3306/sqlalchemy", pool_size=10, max_overflow=20)
    engine = create_engine("sqlite:///../sqlalchemy_test")
    size = 100000
    queries = [None] * size
    with engine.begin() as conn:
        meta.create_all(engine)

        for i in range(size):
            queries[i] = conn.execute(t1.insert(), {"name": f"some name {i}"})

    with engine.begin() as conn:
        #result = conn.execute(select(t1))
        #print(result.fetchall())
        conn.execute(t1.delete())

    engine.dispose()


if __name__ == "__main__":
    main()
