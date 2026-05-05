from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from src.user.model import UserModel
from src.comments.model import CommentModel
from src.likes.model import LikeModel
from src.posts.model import PostModel

def delete_post(post_id:int,db:Session,user:UserModel):
    post=db.query(PostModel).filter(PostModel.id==post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    db.delete(post)
    db.commit()
    return None

def delete_comment(comment_id:int,db:Session,user:UserModel):
    comment=db.query(CommentModel).filter(CommentModel.id==comment_id).first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Comment not found")
    db.delete(comment)
    db.commit()
    return None

def get_all_users(db:Session,user:UserModel):
    users=db.query(UserModel).all()
    return users