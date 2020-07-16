
'''
 * @author Munene Collins
 * 
 * * Created:   16.07.2020
 * 
 * (c) Copyright by Devligence Limited.
 * 
 '''
from sqlalchemy import Column, Integer, String
from database import Base

# User Database Model
class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    fullname = Column(String, unique=True)

# Items Databse Model
class ItemInfo(Base):
    __tablename__ = "item_info"

    id = Column(Integer, primary_key=True, index=True)
    itemname = Column(String, unique=True)
    itemprice = Column(Integer)

# User Cart Databse Model
class CartInfo(Base):
    __tablename__ = "cart_info"

    id = Column(Integer, primary_key=True, index=True)
    ownername = Column(Integer, unique=True)
    itemname = Column(String, unique=True)
    itemprice = Column(Integer)