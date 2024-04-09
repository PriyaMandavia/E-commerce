from sqlalchemy.orm import Session
from app.authentication import schema
import model
from uuid import uuid4
from app.authentication.utils import hash_pass,verify_password
from fastapi import HTTPException,status,Depends
from fastapi.encoders import jsonable_encoder
from app.authentication.dependancy import oauth2_scheme,verify_token_access
from database import get_db

def createuser(db : Session ,user : schema.CreateUser=Depends()):
    hassed_passs = hash_pass(user.password)
    user.password = hassed_passs
    
    new_data = model.User(id = uuid4() , username = user.username ,
                          user_email = user.user_email, password = user.password)
    
    
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data


def loginuser( db: Session,userlogin:schema.LoginUser=Depends()):
    user = db.query(model.User).filter(model.User.user_email == userlogin.user_email).first()
    if not user:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"user not exits")
    if not verify_password(userlogin.password,user.password):
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="password not match")
    return jsonable_encoder(user)




def get_current_user(token: str = Depends(oauth2_scheme),db:Session=Depends(get_db) ):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not Validate Credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    token = verify_token_access(token, credentials_exception)
    user = db.query(model.User).filter(model.User.id == token.id).first()

    return {"user" : user}

def get_current_active_user(current_user: schema.CreateUser = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=400, detail="Inactive user")
    return {"current_user" : current_user}