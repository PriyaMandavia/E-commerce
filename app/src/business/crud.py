from sqlalchemy.orm import Session
from app.src.business import schema
import model
from uuid import uuid4
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException,status



def createdata(data : schema.CreateBusiness , db: Session):
    query = model.Business(id = uuid4(), business_name = data.business_name,
                                            city = data.city,
                                            region = data.region,
                                            business_description = data.business_description,
                                            logo = data.logo, 
                                            owner_id = data.owner_id)
    

    db.add(query)
    db.commit()
    db.refresh(query)
    return {"status" : "Sucess" , "data" : query}


def showdata(limit : int,page : int,db : Session):
    offset = (page-1) * limit
    query = db.query(model.Business).limit(limit).offset(offset).all()
    count = db.query(model.Business).count()
    return query,count


def showdatabyname(name : str ,limit : int,page : int,db : Session):
    offset = (page-1) * limit
    query = db.query(model.Business).filter(model.Business.business_name.like(f"{name}%")).limit(limit).offset(offset).all()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    count = db.query(model.Business).count()
    return query,count



def deletedata(deleteid : str, db: Session):
    query = db.query(model.Business).filter(model.Business.id == deleteid).delete()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.commit()
    return {"message" : "Sucessfully delete the data"}

def updatedata(updateid : str , db:Session , data : schema.UpdateBusiness):
    query = db.query(model.Business).filter(model.Business.id == updateid).first()

    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    query.business_name = data.business_name if data.business_name else query.business_name
    query.business_description = data.business_description if data.business_description else query.business_description
    query.city = data.city if data.city else query.city
    query.logo = data.logo if data.logo else query.logo
    query.region = data.region if data.region else query.region
    query.owner_id = data.owner_id if data.owner_id else query.owner_id
    
    db.commit()
    db.refresh(query)
    return query

