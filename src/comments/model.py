from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.db import Base

class CommentModel(Base):
    __tablename__="comment_table"
    id=Column(Integer, primary_key=True)
    body=Column(String,nullable=False)
    user_id=Column(Integer,ForeignKey("user_table.id",ondelete="CASCADE"),nullable=False)
    post_id=Column(Integer,ForeignKey("post_table.id",ondelete="CASCADE"),nullable=False)
    post=relationship("PostModel",back_populates="comments")
    author=relationship("UserModel",back_populates="comments")