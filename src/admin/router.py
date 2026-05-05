from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.user.model import UserModel
from src.user.dtos import UserResponseSchema
from src.utils.db import get_db
from src.utils.helper import is_admin
from src.admin import controller
from typing import List

admin_routes=APIRouter(prefix="/admin")

@admin_routes.delete("/delete_post/{post_id}",response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_admin)):
    return controller.delete_post(post_id,db,user)

@admin_routes.delete("/delete_comment/{comment_id}",response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(comment_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_admin)):
    return controller.delete_comment(comment_id,db,user)

@admin_routes.get("/all_users",response_model=List[UserResponseSchema],status_code=status.HTTP_200_OK)
def get_all(db:Session=Depends(get_db),user:UserModel=Depends(is_admin)):
    return controller.get_all_users(db,user)