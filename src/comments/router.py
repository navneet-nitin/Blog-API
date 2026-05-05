from fastapi import APIRouter, Depends, status,HTTPException
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.utils.helper import is_authenticated
from src.user.model import UserModel
from src.comments.model import CommentModel
from src.comments.dtos import CommentResponseSchema, CommentSchema
from src.comments import controller
from typing import List

comment_routes=APIRouter(prefix="/comment")

@comment_routes.post("/create/{post_id}",response_model=CommentResponseSchema,status_code=status.HTTP_201_CREATED)
def create_comment(post_id:int,body:CommentSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.create_comment(post_id,body,db,user)

@comment_routes.put("/edit/{comment_id}",response_model=CommentResponseSchema,status_code=status.HTTP_200_OK)
def edit_comment(comment_id:int,body:CommentSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.edit_comment(comment_id,body,db,user)

@comment_routes.delete("/delete/{comment_id}",response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(comment_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.delete_comment(comment_id,db,user)

@comment_routes.get("/all/{post_id}",response_model=List[CommentResponseSchema],status_code=status.HTTP_200_OK)
def get_post_comment(post_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.get_post_comments(post_id,db,user)