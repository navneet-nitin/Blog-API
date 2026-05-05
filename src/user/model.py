from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.utils.db import Base

class UserModel(Base):
    __tablename__="user_table"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    username=Column(String,nullable=False,unique=True) 
    hash_password=Column(String,nullable=False) 
    email=Column(String,nullable=False,unique=True)
    mobile_no=Column(String,nullable=False)
    role=Column(String,default="user")
    posts=relationship("PostModel",back_populates="author")
    comments=relationship("CommentModel",back_populates="author")