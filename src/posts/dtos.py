from pydantic import BaseModel, ConfigDict

class PostSchema(BaseModel):
    title:str
    body:str
    category:str

class PostResponseSchema(BaseModel):
    id: int
    title: str
    body: str
    category: str
    status: str
    user_id: int
    model_config=ConfigDict(from_attributes=True)