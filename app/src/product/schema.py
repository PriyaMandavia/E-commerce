from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreateProduct(BaseModel):
    name :Optional[str]
    category :Optional[str]
    original_price : Optional[int] 
    new_price : Optional[int]
    percentage_discount : Optional[int]
    offer_expiration_date : Optional[datetime]
    product_image :Optional[str]
    date_published :Optional[datetime] 
    business_id : Optional[str] 
    class Config:
        from_attributes = True


class UpdateProduct(BaseModel):
    name :Optional[str] = None
    category :Optional[str] = None
    original_price : Optional[int] = None
    new_price : Optional[int]=None
    percentage_discount : Optional[int]=None
    offer_expiration_date : Optional[datetime]=None
    product_image :Optional[str]=None
    date_published :Optional[datetime]=None
    business_id : Optional[str]= None
    class Config:
        from_attributes = True
