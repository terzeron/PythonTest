#!/usr/bin/env python

from sqlalchemy import Table, Column, insert, Integer, String, MetaData, create_engine, select, ForeignKey
from sqlalchemy.orm import registry, relationship
from pprint import pprint

mapper_registry = registry()
Base = mapper_registry.generate_base()

engine = create_engine("sqlite+pysqlite:///sqlalchemy_test", echo=True, future=True)


class User(Base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


mapper_registry.metadata.create_all(engine)

user_table = Table("user_account", mapper_registry.metadata, autoload_with=engine)
address_table = Table("address", mapper_registry.metadata, autoload_with=engine)

stmt = insert(user_table).values(name='spongebob', fullname='Spongebob Squarepants')
pprint(stmt)
print(stmt)

compiled = stmt.compile()
pprint(compiled.params)

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()

pprint(result.inserted_primary_key)

with engine.connect() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"},
        ])
    conn.commit()

    select_stmt = select(user_table.c.id, user_table.c.name + '@aol.com')
    result = conn.execute(select_stmt)
    for row in result:
        print(row)
    insert_stmt = insert(address_table).from_select(
        ["user_id", "email_address"], select_stmt)
    # print(insert_stmt)
    result = conn.execute(insert_stmt)

    # insert_stmt = insert(address_table).returning(address_table.c.id, address_table.c.email_address)
    # print(insert_stmt)
    # print(insert_stmt)
    # result = conn.execute(insert_stmt)

    conn.commit()

    select_stmt = select(user_table.c.id, user_table.c.name)
    result = conn.execute(select_stmt)
    for row in result:
        print(row)
