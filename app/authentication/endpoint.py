from fastapi import APIRouter,Depends,HTTPException,status
from database import get_db
from app.authentication import schema,crud
from sqlalchemy.orm import Session
from app.authentication.dependancy import create_access_token
from typing import Any


router = APIRouter(prefix="/user" , tags=["Authentication"])


@router.post("/createuser" , response_model=schema.UserResponse,status_code=status.HTTP_201_CREATED)
def create_user(user : schema.CreateUser=Depends() , db : Session = Depends(get_db)):
    try:
        result = crud.createuser(user=user,db=db)
        return result
    except Exception:
        raise HTTPException(status_code=400, detail="Email already registered")
    

@router.post('/login',response_model=schema.Token)
def loginuserdetail(userdetail:schema.LoginUser=Depends(), db: Session = Depends(get_db)):
    try:
        login = crud.loginuser(db=db,userlogin=userdetail)
        access_token =create_access_token(data={"user_id":login["id"]}) 
        return {"access_token" : access_token,"token_type" : "bearer"}


    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Unmatched")
    

@router.get("/users/me/")
def read_users_me(current_user: Any= Depends(crud.get_current_active_user)):
    return {"current" : current_user}

