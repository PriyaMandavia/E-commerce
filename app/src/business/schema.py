from pydantic import BaseModel
from typing import Optional,List


class CreateBusiness(BaseModel):
    business_name : Optional[str]
    city : Optional[str]
    region : Optional[str]
    business_description : Optional[str]
    logo : Optional[str]
    owner_id : Optional[str]
    class Config:
        from_attributes = True
    

class BusinessResponse(BaseModel):
    status : str
    data : List[CreateBusiness]  
    page : int
    class Config:
        from_attributes = True 


class BusinessOutput(BaseModel):
    status : str
    data : List[CreateBusiness]
    class Config:
        from_attributes = True


class UpdateBusiness(BaseModel):
    business_name : Optional[str] = None
    city : Optional[str] = None
    region : Optional[str] = None
    business_description : Optional[str]=None 
    logo : Optional[str] =None
    owner_id : Optional[str]=None
    class Config:
        from_attributes = True