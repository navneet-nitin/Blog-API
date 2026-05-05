from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.posts.model import PostModel
from src.posts.dtos import PostSchema, PostResponseSchema
from src.user.model import UserModel
from src.utils.helper import is_authenticated
from src.posts import controller
from src.utils.db import get_db
from typing import List

post_routes=APIRouter(prefix="/post")

@post_routes.post("/create")
def create_post(body:PostSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.create_post(body,db,user)

@post_routes.put("/publish/{post_id}")
def publish_post(post_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.publish_post(post_id,db,user)

@post_routes.get("/all")
def get_all_post(limit:int=10,offset:int=0,category:str=None,db:Session=Depends(get_db),username:str=None,user:UserModel=Depends(is_authenticated)):
    return controller.get_all_post(limit,offset,category,db,username,user)

@post_routes.get("/get_post/{post_id}",response_model=List[PostResponseSchema],status_code=status.HTTP_202_ACCEPTED)
def get_post(post_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.get_post(post_id,db,user)

@post_routes.get("/get_my_posts",response_model=List[PostResponseSchema],status_code=status.HTTP_200_OK)
def get_my_posts(db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.get_my_post(db,user)
    
@post_routes.put("/update/{post_id}",response_model=PostResponseSchema,status_code=status.HTTP_202_ACCEPTED)
def update(post_id:int,body:PostSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.update(post_id,body,db,user)

@post_routes.delete("/delete/{post_id}")
def delete(post_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.delete(post_id,db,user)