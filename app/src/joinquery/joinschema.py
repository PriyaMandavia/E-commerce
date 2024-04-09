from pydantic import BaseModel
from app.src.business import schema as Businessschema
from app.src.product import schema as Productschema
from app.src.owner import schema as Ownerschema
from typing import Optional,List
from datetime import datetime

class Show(BaseModel):
   
   business_name : Optional[str]
   ownername : Optional[str]
   city : Optional[str]
   business_description : Optional[str]
   is_verifide : Optional[bool] 
   class Config :
      from_attributes = True

class Result(BaseModel):
   status : str
   total : int
   data : List[Show]
   class Config:
      from_attributes =True   


class Show_data(BaseModel):
   business_name : Optional[str]
   ownername : Optional[str]
   city : Optional[str]
   category :Optional[str] = None
   original_price : Optional[int] = None
   new_price : Optional[int]=None
   percentage_discount : Optional[int]=None
   offer_expiration_date : Optional[datetime]=None
   class Config:
      from_attributes =True   


class AlldataResponse(BaseModel):
   status : str
   total : int
   data : List[Show_data]
   class Config:
      from_attributes =True   


class AllTable(BaseModel):
   business : List[Businessschema.CreateBusiness] 
   product : List[Productschema.CreateProduct]
   owner : List[Ownerschema.CreateOwner]
   class Config:
      from_attributes : True


class DataResponse(BaseModel):
   alldata : List[AllTable]
   class Config:
      from_attributes : True






