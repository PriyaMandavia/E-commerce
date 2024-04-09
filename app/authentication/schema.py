from pydantic import BaseModel,EmailStr
from  typing import Optional


class CreateUser(BaseModel):
    username : str
    user_email : EmailStr
    password : str 
    class Config:
        from_attributes : True   

class UserResponse(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str


class DataToken(BaseModel):
    id: Optional[str] = None

class LoginUser(BaseModel):
    user_email : EmailStr
    password  : str  
    class Config:
        from_attributes : True   
  