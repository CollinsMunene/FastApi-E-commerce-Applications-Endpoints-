from typing import List
from pydantic import BaseModel

class UserInfoBase(BaseModel):
    username:str
    fullname:str

class UserCreate(UserInfoBase):
    password:str

class UserLogin(BaseModel):
    username:str
    password:str

class UserInfo(UserInfoBase):
    id:int

    class Config:
        orm_mode = True

class ItemInfo(BaseModel):
    itemname:str
    itemprice:int

class ItemAInfo(ItemInfo):
    id:int

    class Config:
        orm_mode = True