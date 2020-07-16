from typing import List

import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException

import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/register", response_model=schemas.UserInfo)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.post("/login")
def login_user(user:schemas.UserLogin, db:Session = Depends(get_db)):
    db_user = crud.get_Login(db, username=user.username, password=user.password)
    if db_user == False :
        raise HTTPException(status_code=400, detail="Wrong username/password")
    return {"message":"User found"}

@app.get("/getuser/{username}", response_model=schemas.UserInfo)
def get_user(username, db:Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=username)
    return db_user

@app.post("/addItem", response_model=schemas.ItemInfo)
def add_item(item: schemas.ItemInfo, db: Session = Depends(get_db)):
    db_item = crud.add_table(db=db, item=item)
    if db_item:
        raise HTTPException(status_code=200, detail="item registered")
    return 

@app.get("/getitem/{id}", response_model=schemas.ItemAInfo)
def get_user(id, db:Session = Depends(get_db)):
    db_item = crud.get_item_by_id(db, id=id)
    if db_item is None:
        raise HTTPException(status_code=400, detail="No item found")
    return db_item

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8081)