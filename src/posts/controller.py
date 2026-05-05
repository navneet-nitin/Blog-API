'''
o	create_post() — creates with status "draft", user_id=user.id
o	publish_post() — checks ownership, changes status to "published"
o	get_all_posts() — only published posts, with limit and offset for pagination, filter by category and username if provided
o	get_single_post() — returns one post by id, must be published or owned by requester
o	get_my_posts() — returns all posts by logged in user including drafts
o	update_post() — check ownership, update fields
o	delete_post() — check ownership, delete
'''
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.posts.model import PostModel
from src.posts.dtos import PostSchema
from src.user.model import UserModel


def create_post(body:PostSchema,db:Session,user:UserModel):
    data=PostModel(title=body.title,body=body.body,category=body.category,status="draft",user_id=user.id)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def publish_post(post_id:int,db:Session,user:UserModel):
    data=db.query(PostModel).filter(PostModel.id==post_id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Post Found")
    if data.user_id!=user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You are not allowed to publish")
    data.status="published"
    db.commit()
    db.refresh(data)

    return data


def get_all_post(limit:int,offset:int,category:str,db:Session,username:str,user:UserModel):
    data=db.query(PostModel).filter(PostModel.status=="published")
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Posts not found")
    if category:
        data=db.query(PostModel).filter(PostModel.category==category)
    if username:
        data= data.join(UserModel).filter(UserModel.username == username)
    posts=data.offset(offset).limit(limit).all()
    return posts

def get_post(post_id:int,db:Session,user:UserModel):
    data=db.query(PostModel).filter(PostModel.id==post_id).first()
    if data.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are not unauthorized")
    if data.status != "published":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    return data

def get_my_post(db:Session,user:UserModel):
    data=db.query(PostModel).filter(PostModel.user_id==user.id).all()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    return data

def update(post_id:int,body:PostSchema,db:Session,user:UserModel):
    data=db.query(PostModel).filter(PostModel.id==post_id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    if data.user_id!=user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are not authorized")
    data.title=body.title
    data.body=body.body
    data.category=body.category

    db.commit()
    db.refresh(data)
    return data
    
def delete(post_id:int,db:Session,user:UserModel):
    data=db.query(PostModel).filter(PostModel.id==post_id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    if data.user_id!=user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are not authorized to delete this post")
    db.delete(data)
    db.commit()
    return None
