from sqlalchemy.orm import Session
from app.src.product import schema
import model
from uuid import uuid4
from fastapi import HTTPException,status

def createproduct(product : schema.CreateProduct,db : Session):
    query = model.Product(id = uuid4(), name = product.name,
                                        category = product.category,    
                                        original_price =product.original_price, 
                                        new_price = product.new_price,
                                        percentage_discount = product.percentage_discount,
                                        offer_expiration_date = product.offer_expiration_date,
                                        product_image  = product.product_image,
                                        date_published = product.date_published, 
                                        business_id = product.business_id)
    
    db.add(query)
    db.commit()
    db.refresh(query)
    return {"status" : "Success" , "Product" : query}

def showproduct(limit : int , page : int , db: Session):
    offset = (page-1)*limit
    query = db.query(model.Product).limit(limit).offset(offset).all()
    count = db.query(model.Product).count()
    return query , count

def showproductbyname(name:str,limit : int , page : int , db: Session):
    offset = (page-1)*limit
    query = db.query(model.Product).filter(model.Product.name.like(f"{name}%")).limit(limit).offset(offset).all()
    count = db.query(model.Product).count()
    return query , count


def deletedata(deleteid : str , db: Session):
    query = db.query(model.Product).filter(model.Product.id == deleteid).delete()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.commit()
    return {"Message" : "Successfully delete the data"}

def updatedata(updateid : str , update_data : schema.UpdateProduct , db : Session):
    data = db.query(model.Product).filter(model.Product.id == updateid).first()
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
 
    data.name = update_data.name if update_data else data.name
    data.category = update_data.category if update_data.category else data.category
    data.original_price = update_data.original_price if update_data.original_price else data.original_price
    data.new_price = update_data.new_price if update_data.new_price else data.new_price
    data.percentage_discount = update_data.percentage_discount if update_data.percentage_discount else   data.percentage_discount
    data.offer_expiration_date = update_data.offer_expiration_date if update_data.offer_expiration_date else data.offer_expiration_date
    data.product_image = update_data.product_image if update_data.product_image else data.product_image
    data.date_published = update_data.date_published if update_data.date_published else data.date_published
    data.business_id = update_data.business_id if update_data.business_id else data.business_id


    db.commit()
    db.refresh(data)
    return {"status" : "Success" , "data" : data}


     