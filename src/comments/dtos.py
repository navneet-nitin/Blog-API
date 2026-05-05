from pydantic import BaseModel, ConfigDict


class CommentSchema(BaseModel):
    body:str

class CommentResponseSchema(BaseModel):
    id:int
    body:str
    user_id:int
    post_id:int
    model_config=ConfigDict(from_attributes=True)