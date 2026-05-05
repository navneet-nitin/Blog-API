from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.db import Base

class LikeModel(Base):
    __tablename__="like_table"
    user_id=Column(Integer,ForeignKey("user_table.id",ondelete="CASCADE"),primary_key=True,nullable=False)
    post_id=Column(Integer,ForeignKey("post_table.id",ondelete="CASCADE"),primary_key=True,nullable=False)
    #When you mark both columns as primary_key=True, SQLAlchemy automatically treats them as a composite primary key.
    post=relationship("PostModel",back_populates="likes")