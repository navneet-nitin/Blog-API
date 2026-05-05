from fastapi import Depends, APIRouter, status, HTTPException
from src.user.dtos import UserSchema, UserResponseSchema, LoginSchema
from src.user.model import UserModel
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.utils.helper import is_authenticated
from src.user import controller

user_routes=APIRouter(prefix="/user")

@user_routes.post("/register",response_model=UserResponseSchema,status_code=status.HTTP_201_CREATED)
def register(body:UserSchema, db:Session=Depends(get_db)):
    return controller.register(body,db)

@user_routes.get("/login")
def login(body:LoginSchema,db:Session=Depends(get_db)):
    return controller.login(body,db)

@user_routes.get("/profile")
def profile(user:UserModel=Depends(is_authenticated)):
    return controller.get_profile(user)

@user_routes.put("/update",response_model=UserResponseSchema, status_code=status.HTTP_202_ACCEPTED)
def update(body:UserSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.update(body,db,user)

@user_routes.delete("/delete",response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete(db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.delete(db,user)