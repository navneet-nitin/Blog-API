from fastapi import Depends, HTTPException, status
from src.user.model import UserModel
from src.user.dtos import UserSchema, LoginSchema
from src.utils.db import get_db
from src.utils.settings import settings
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from datetime import datetime, timedelta
import jwt

password_hash = PasswordHash.recommended()

def create_password_hash(password):
    return password_hash.hash(password=password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)



def register(body:UserSchema,db:Session):
    username_present=db.query(UserModel).filter(UserModel.username==body.username).first()
    if username_present:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Username already exists")
    email_present=db.query(UserModel).filter(UserModel.email==body.email).first()
    if email_present:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Email already exists!!")
    hashed_password=create_password_hash(body.password)
    data=UserModel(name=body.name,username=body.username,hash_password=hashed_password,email=body.email,mobile_no=body.mobile_no,role="user")
    db.add(data)
    db.commit()
    db.refresh(data)

    return data

def login(body:LoginSchema,db:Session):
    data=db.query(UserModel).filter(UserModel.username==body.username).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Username not found")
    password_match=verify_password(body.password,data.hash_password)
    if not password_match:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Password not matched")
    expiry_time=datetime.now()+timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token=jwt.encode({"id":data.id,"exp":expiry_time.timestamp()},settings.SECRET_KEY,settings.ALGORITHM)
    return {
        "token":token
    }


def get_profile(user:UserModel):
    return user

def update(body:UserSchema,db:Session,user:UserModel):
    user.name=body.name
    user.email=body.email
    user.mobile_no=body.mobile_no
    db.commit()
    db.refresh(user)

    return user
    
def delete(db:Session,user:UserModel):
    db.delete(user)
    db.commit()
    return None