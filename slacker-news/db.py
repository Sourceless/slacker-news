import hashlib
import pbkdf2
import random
import slackernews.security as security
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

# Change later, to be taken from config
engine = create_engine('sqlite:///:memory', echo=True)

# Base class for ORM objects
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    description = Column(Text)
    key = Column(String(128))
    salt = Column(String(128))

    def __init__(self, name, password, fullname='', description=''):
        self.name = name
        self.fullname = fullname
        self.description = description
        self.salt = security.random_salt(128)
