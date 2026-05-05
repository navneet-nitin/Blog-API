from fastapi import Depends,status, APIRouter
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.utils.helper import is_authenticated
from src.user.model import UserModel
from src.likes import controller
from src.likes.dtos import LikeResponseSchema

like_routes=APIRouter(prefix="/like")

@like_routes.post("/create/{post_id}",response_model=LikeResponseSchema,status_code=status.HTTP_200_OK)
def like_post(post_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.like_post(post_id,db,user)

@like_routes.delete("/unlike/{post_id}",response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def unlike(post_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.unlike(post_id,db,user)

@like_routes.get("/total/{post_id}",response_model=int,status_code=status.HTTP_200_OK)
def total_likes(post_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.get_like_count(post_id,db,user)