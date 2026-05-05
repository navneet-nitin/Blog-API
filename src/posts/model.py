from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.db import Base

class PostModel(Base):
    __tablename__="post_table"
    id=Column(Integer,primary_key=True)
    title=Column(String,nullable=False)
    body=Column(String,nullable=False)
    category=Column(String,nullable=False)
    status=Column(String,default="draft")
    user_id=Column(Integer,ForeignKey("user_table.id",ondelete="CASCADE"),nullable=False)
    author=relationship("UserModel",back_populates="posts")
    likes=relationship("LikeModel",back_populates="post",cascade="all, delete")
    comments=relationship("CommentModel",back_populates="post",cascade="all, delete")