
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    wallet_balance = Column(Float, default=0.0)

class ProjectContainer(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    is_active = Column(Boolean, default=True)

class StoreAddon(Base):
    __tablename__ = 'store_addons'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float)
    tx_type = Column(String) # deposit, withdraw, purchase
