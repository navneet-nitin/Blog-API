from fastapi import FastAPI
from src.user.model import UserModel
from src.comments.model import CommentModel
from src.likes.model import LikeModel
from src.posts.model import PostModel
from src.utils.db import Base,engine
from src.user.router import user_routes
from src.posts.router import post_routes
from src.comments.router import comment_routes
from src.likes.router import like_routes
from src.admin.router import admin_routes

#Base.metadata.create_all(engine) 

app=FastAPI()
app.include_router(user_routes)
app.include_router(post_routes)
app.include_router(comment_routes)
app.include_router(like_routes)
app.include_router(admin_routes)