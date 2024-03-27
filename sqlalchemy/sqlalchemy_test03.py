#!/usr/bin/env python

from sqlalchemy import create_engine, text
from sqlalchemy import MetaData

metadata_obj = MetaData()

from sqlalchemy import Table, Column, Integer, String, ForeignKey

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)
from pprint import pprint

pprint(user_table.c.name)
pprint(user_table.c.keys())
pprint(user_table.primary_key)

engine = create_engine("sqlite+pysqlite:///sqlalchemy_test", echo=True, future=True)
metadata_obj.create_all(engine)

from sqlalchemy.orm import registry

mapper_registry = registry()
pprint(mapper_registry.metadata)
Base = mapper_registry.generate_base()

from sqlalchemy.orm import relationship


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


pprint(User.__table__)

sandy = User(name="sandy", fullname="Sandy Cheeks")
pprint(sandy)

mapper_registry.metadata.create_all(engine)

Base.metadata.create_all(engine)

mapper_registry = registry()
Base.metadata.create_all(engine)

user = Table("user_account", metadata_obj, autoload_with=engine)
pprint(user)
