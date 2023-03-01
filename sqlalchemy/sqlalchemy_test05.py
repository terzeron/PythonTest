#!/usr/bin/env python

from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, select, ForeignKey, insert
from sqlalchemy.orm import registry, relationship, Session
from pprint import pprint

# import logging

# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)

mapper_registry = registry()
Base = mapper_registry.generate_base()

engine = create_engine("sqlite+pysqlite:///sqlalchemy_test", echo=False, future=True)


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

with engine.connect() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"},
            {"name": "spongebob", "fullname": "Spongebob Squarepants"},
        ])
    conn.commit()

stmt = select(user_table).where(user_table.c.name == 'spongebob')
print(stmt)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        pprint(row)

stmt = select(User).where(User.name == 'spongebob')
with Session(engine) as session:
    for user_obj in session.execute(stmt):
        pprint(user_obj)

    row = session.execute(select(User)).first()
    pprint(row)
    pprint(row[0])

    user = session.scalars(select(User)).first()
    pprint(user)

print(select(user_table))
print(select(user_table.c.name, user_table.c.fullname))
print(select(User))

stmt = (
    select(
        ("UserName: " + user_table.c.name).label("username"),
    ).order_by(user_table.c.name)
)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(f"{row.username}")
