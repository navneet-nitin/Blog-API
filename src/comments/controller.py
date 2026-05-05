from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from src.comments.model import CommentModel
from src.posts.model import PostModel
from src.comments.dtos import CommentSchema
from src.user.model import UserModel



def create_comment(post_id:int,body:CommentSchema,db:Session,user:UserModel):
    post_present=db.query(PostModel).filter(PostModel.id==post_id).first()
    if not post_present:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post Not Found")
    data=CommentModel(user_id=user.id,body=body.body,post_id=post_id)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def delete_comment(comment_id:int,db:Session,user:UserModel):
    data=db.query(CommentModel).filter(CommentModel.id==comment_id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Comment not found")
    if data.user_id!=user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are not authorized to delete this comment")
    db.delete(data)
    db.commit()
    return None

def get_post_comments(post_id:int,db:Session,user:UserModel):
    post_present=db.query(PostModel).filter(PostModel.id==post_id).first()
    if not post_present:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post Not Found")
    data=db.query(CommentModel).filter(CommentModel.post_id==post_id).all()
    return data

def edit_comment(comment_id:int,body:CommentSchema,db:Session,user:UserModel):
    data=db.query(CommentModel).filter(CommentModel.id==comment_id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Comment not found")
    data.body=body.body
    db.commit()
    db.refresh(data)
    return data