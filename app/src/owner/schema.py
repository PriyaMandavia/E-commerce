from pydantic import BaseModel,EmailStr
from typing import Optional,List
from datetime import datetime


class CreateOwner(BaseModel):
    ownername : Optional[str]
    email : Optional[EmailStr]
    password : Optional[str]
    is_verifide : Optional[bool]
    join_date : Optional[datetime]

    
   
    class Config:
        from_attributes = True
    

class OwnerResponse(BaseModel):
    status : str
    data : List[CreateOwner]  
    class Config:
        from_attributes = True     

class UpdateOwner(BaseModel):
    ownername : Optional[str] =None
    email : Optional[EmailStr] =None
    password : Optional[str]=None
    is_verifide : Optional[bool] =None
    
    class Config:
        from_attributes = True
    
