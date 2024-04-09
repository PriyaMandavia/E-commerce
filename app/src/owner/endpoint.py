from database import get_db
from sqlalchemy.orm import Session
from app.src.owner import crud,schema
from fastapi import APIRouter,HTTPException,status,Depends
from app.authentication.dependancy import oauth2_scheme,verify_token_access


router = APIRouter(prefix="/owner" , tags=["Owner"])


@router.post("/createowner" , status_code=status.HTTP_201_CREATED)
def create_owner(owner : schema.CreateOwner ,token : str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not Validate Credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    token = verify_token_access(token, credentials_exception)
    try:
        result = crud.createowner(owner=owner,db=db)
        return result
    except Exception as e :
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , 
                            detail=f"owner is not created : {type(e).__name__}")


@router.get("/show_owner" , status_code=status.HTTP_202_ACCEPTED)
def show_owner(limit : int = 2, page : int =1, db:Session=Depends(get_db)):
    try:
        result , count = crud.showowner(limit=limit,page=page,db=db)
        return {"status" : "sucess" , "data" : result , "total" : count}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Not found the data")
    
@router.get("/show_owner{name}" , status_code=status.HTTP_202_ACCEPTED)
def show_owner(name : str ,limit : int = 2, page : int =1, db:Session=Depends(get_db)):
    try:
        result , count = crud.showownerbyname(name=name ,limit=limit,page=page,db=db)
        return {"status" : "sucess" , "data" : result , "total" : count}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= f"not found the data")
    

@router.delete("/delete_data{id}" ,status_code=status.HTTP_200_OK)
def delete_data(deleteid:str,token : str = Depends(oauth2_scheme), db:Session=Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not Validate Credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    token = verify_token_access(token, credentials_exception)
    try:
        result = crud.deleteowner(deleteid=deleteid , db=db)
        return result
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not found the data")
    
@router.put("/update_data{id}")
def updatedata(updateid : str , upadet : schema.UpdateOwner,token : str = Depends(oauth2_scheme),db:Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not Validate Credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    token = verify_token_access(token, credentials_exception)
    try:
        result = crud.updateowner(updateid=updateid, update=upadet , db=db)
        return {"status" : "Success" , "data" : result}
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Not found data")    