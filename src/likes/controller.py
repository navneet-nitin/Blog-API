from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from src.likes.model import LikeModel
from src.posts.model import PostModel
from src.likes.dtos import LikeResponseSchema
from src.user.model import UserModel

def like_post(post_id:int,db:Session,user:UserModel):
    post_exist=db.query(PostModel).filter(PostModel.id==post_id).first()
    if not post_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post Not Found!")
    like_exist=db.query(LikeModel).filter(LikeModel.post_id==post_id, LikeModel.user_id==user.id).first()
    if like_exist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Already liked the post")
    like_post=LikeModel(user_id=user.id,post_id=post_id)
    db.add(like_post)
    db.commit()
    db.refresh(like_post)
    return like_post

def unlike(post_id:int,db:Session,user:UserModel):
    post=db.query(LikeModel).filter(LikeModel.post_id==post_id, LikeModel.user_id==user.id).first()
    if not post:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="There was no like to this post by you.")
    db.delete(post)
    db.commit()
    return None

def get_like_count(post_id:int,db:Session,user:UserModel):
    like_count=db.query(LikeModel).filter(LikeModel.post_id==post_id).count()
    return like_count
    