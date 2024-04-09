from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from app.src.owner import schema
import model
from uuid import uuid4
from app.authentication.utils import hash_pass

def createowner(owner : schema.CreateOwner, db: Session):
    hshed_password = hash_pass(owner.password)
    password = hshed_password
    
    query = model.Owner(id = uuid4(),ownername = owner.ownername,
                                    email = owner.email,
                                    password = password,
                                    is_verifide = owner.is_verifide,
                                    join_date = owner.join_date

                                    )
    
    db.add(query)
    db.commit()
    db.refresh(query)
    return {"status" : "Sucess" , "data" : query}


def showowner(limit: int , page : int ,db: Session):
    offset = (page-1)*limit
    query = db.query(model.Owner).limit(limit).offset(offset).all()
    count = db.query(model.Owner).count()
    return query,count


def showownerbyname(name : str,limit: int , page : int ,db: Session):
    offset = (page-1)*limit
    query = db.query(model.Owner).filter(model.Owner.ownername.like(f"{name}%")).limit(limit).offset(offset).all()
    if not query:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    count = db.query(model.Owner).count()
    return query,count


def deleteowner(deleteid : str , db:Session):
    query = db.query(model.Owner).filter(model.Owner.id == deleteid).delete()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.commit()
    return {"message" : "Successfully delete the data"}

def updateowner(updateid : str , db: Session , update : schema.UpdateOwner):
    query = db.query(model.Owner).filter(model.Owner.id == updateid).first()

    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    query.ownername = update.ownername if update.ownername else query.ownername
    query.is_verifide = update.is_verifide if update.is_verifide else query.is_verifide
    query.email = update.email if update.email else query.email
    query.password = update.password if update.password else query.password


    db.commit()
    db.refresh(query)
    return query