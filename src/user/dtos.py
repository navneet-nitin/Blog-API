from pydantic import BaseModel, ConfigDict

class UserSchema(BaseModel):
    name:str
    username:str
    password:str 
    email:str
    mobile_no:str

class UserResponseSchema(BaseModel):
    id:int
    name:str
    username:str
    email:str
    mobile_no:str
    role:str
    model_config=ConfigDict(from_attributes=True)

class LoginSchema(BaseModel):
    username:str
    password:str