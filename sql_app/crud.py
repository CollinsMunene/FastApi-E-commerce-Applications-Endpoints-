'''
 * @author Munene Collins
 * 
 * * Created:   16.07.2020
 * 
 * (c) Copyright by Devligence Limited.
 * 
 '''
 
from sqlalchemy.orm import Session
import models, schemas
import bcrypt
import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime
import base64

# Get user by username function
def get_user_by_username(db: Session, username: str):
    return db.query(models.UserInfo).filter(models.UserInfo.username == username).first()

# User registration function
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.UserInfo(username=user.username, password=hashed_password, fullname=user.fullname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Login Function
def get_Login(db: Session, username: str, password:str):
    db_user = db.query(models.UserInfo).filter(models.UserInfo.username == username).first()
    print(username,password)
    passw = bcrypt.checkpw(password.encode('utf-8'), db_user.password.encode('utf-8')) 
    return passw

# Get item by id function
def get_item_by_id(db: Session, id: int):
    return db.query(models.ItemInfo).filter(models.ItemInfo.id == id).first()

# Add items to DB function
def add_table(db: Session, item: schemas.ItemInfo):
    db_item = models.ItemInfo(itemname=item.itemname,itemprice=item.itemprice)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Delete item from DB by id function
def delete_item_by_id(db: Session, id: int):
    delitem = db.query(models.ItemInfo).filter(models.ItemInfo.id == id).first()
    if delitem is None:
        return
    db.delete(delitem)
    db.commit()
    return delitem

# Add to cart function
def add_to_cart(db: Session, username: str, items:models.CartInfo):
    user = db.query(models.UserInfo).filter(models.UserInfo.username == username).first()
    db_cart = models.CartInfo(ownername=user.id,itemname=items.itemname,itemprice=items.itemprice)
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

# Delete item in the cart by id
def delete_cart_item_by_id(db: Session, id: int):
    delitem = db.query(models.CartInfo).filter(models.CartInfo.id == id).first()
    if delitem is None:
        return
    db.delete(delitem)
    db.commit()
    return delitem

# Mpesa processing function(Not Complete Yet)
def payment(db:Session, phone_number:int,total:int):
    consumer_key = 'consumer_key'
    consumer_secret = 'consumer_secret'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = 'short_code' # replace with the business short code
    passkey = "pass_key"
    data_to_encode = Business_short_code + passkey + lipa_time
    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')

    access_token = validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": Business_short_code,
        "Password": decode_password,
        "Timestamp": lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": total,
        "PartyA": phone_number,
        "PartyB": Business_short_code,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://127.0.0.1:8000/callback", # Mpesa Callback
        "AccountReference": "User Payment",
        "TransactionDesc": "Testing stk push"
    }
    response = requests.post(api_url, json=request, headers=headers)
    return response.text