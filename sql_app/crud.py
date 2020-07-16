from sqlalchemy.orm import Session
import models, schemas
import bcrypt


def get_user_by_username(db: Session, username: str):
    return db.query(models.UserInfo).filter(models.UserInfo.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.UserInfo(username=user.username, password=hashed_password, fullname=user.fullname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_Login(db: Session, username: str, password:str):
    db_user = db.query(models.UserInfo).filter(models.UserInfo.username == username).first()
    print(username,password)
    passw = bcrypt.checkpw(password.encode('utf-8'), db_user.password.encode('utf-8')) 
    return passw

def get_item_by_id(db: Session, id: int):
    return db.query(models.ItemInfo).filter(models.ItemInfo.id == id).first()

def add_table(db: Session, item: schemas.ItemInfo):
    db_item = models.ItemInfo(itemname=item.itemname,itemprice=item.itemprice)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
