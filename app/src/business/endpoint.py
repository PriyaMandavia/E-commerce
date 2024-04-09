from database import get_db
from app.src.business import crud,schema
from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from app.authentication.dependancy import verify_token_access,oauth2_scheme
from app.src.joinquery import joincrud,joinschema

router = APIRouter(prefix="/businessdata" , tags=["Home"])


@router.post("/createdata" , status_code= status.HTTP_201_CREATED)
def create_data(data : schema.CreateBusiness,token : str =Depends(oauth2_scheme),db:Session=Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not Validate Credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    token = verify_token_access(token, credentials_exception)
    try :
        result = crud.createdata(data=data,db=db)
        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"not created data :{type(e).__name__}")
    

@router.get("/show_data" , status_code=status.HTTP_202_ACCEPTED  )
def show_data(limit : int = 2,page : int = 1,db : Session = Depends(get_db)):
    try:
        result , count= crud.showdata(db=db,limit=limit,page=page)
        return {"status" : "sucess" , "data" : result , "total" : count}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= f"Not found data : {type(e).__name__}")
    

@router.get("/show_data{name}" , status_code=status.HTTP_202_ACCEPTED  )
def show_data(name: str ,limit : int = 2,page : int = 1,db : Session = Depends(get_db)):
    try:
        result , count= crud.showdatabyname(name=name ,db=db,limit=limit,page=page)
        return {"status" : "sucess" , "data" : result , "total" : count}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= f"Not found data : {type(e).__name__}")
        


@router.delete("/delete_data{id}" , status_code=status.HTTP_200_OK)
def delete_data(deleteid:str,token : str =Depends(oauth2_scheme),db : Session= Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not Validate Credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    token = verify_token_access(token, credentials_exception)
    try:
        result =crud.deletedata(deleteid=deleteid , db=db)
        return result
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found the data")


@router.put("/update_data{id}" , status_code=status.HTTP_200_OK)
def businessupdate(updateid: str , update : schema.UpdateBusiness ,token : str = Depends(oauth2_scheme),  db:Session=Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not Validate Credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    token = verify_token_access(token, credentials_exception)
    try:
        result = crud.updatedata(updateid=updateid,data=update,db=db)
        return {"status" : "success" , "data" : result}
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= " Not Found the data")
    
###########################---join-----########################
    

@router.get("/get_business_with_ownername{name}" , response_model=joinschema.Result)
def details_business(name : str , limit : int = 2 , page : int =1,db:Session=Depends(get_db)):
    result , count = joincrud.details(name=name ,limit=limit,page=page,db=db )
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= "Not found the data") 
    return {"status" : "success" , "data" : result ,"total" : count}


@router.get("/get_data{name}" , response_model=joinschema.AlldataResponse)
def data_show(name : str , limit : int =2 ,page : int =1 ,db:Session=Depends(get_db)):
    result ,count= joincrud.show_data(name=name,limit=limit,page=page,db=db)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= "Not found the data")
    
    return {"status" : "Success" , "data" : result , "total" : count}






    