from fastapi import APIRouter,HTTPException,status,Depends
from database import get_db
from app.src.product import crud,schema
from sqlalchemy.orm import Session
from app.authentication.dependancy import verify_token_access,oauth2_scheme


router = APIRouter(prefix="/product" , tags=["Product"])


@router.post("/craeteproduct" , status_code=status.HTTP_201_CREATED)
def create_product(product : schema.CreateProduct , token : str = Depends(oauth2_scheme),db : Session= Depends(get_db) ):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not Validate Credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    token = verify_token_access(token, credentials_exception)
    try:
        result = crud.createproduct(product=product , db=db)
        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail= f"product is not create :{type(e).__name__} ")
    
@router.get("/show_product" , status_code=status.HTTP_202_ACCEPTED)
def show_product(limit : int=2 , page : int =1 , db: Session = Depends(get_db)):
    try:
        result , count= crud.showproduct(limit=limit,page=page,db=db)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return {"status" : "sucess" , "data" : result , "total" : count}
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = "Not found the product")    
    

@router.get("/show_product{name}" , status_code=status.HTTP_202_ACCEPTED)
def show_productbyname(name : str ,limit : int=2 , page : int =1 , db: Session = Depends(get_db)):
    try:
        result , count= crud.showproductbyname(name=name ,limit=limit,page=page,db=db)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return {"status" : "sucess" , "data" : result , "total" : count}
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = "Not found the product")    
        
    

@router.delete("/delete_product{id}" , status_code=status.HTTP_200_OK)
def delete_product(deleteid : str , token : str = Depends(oauth2_scheme),db:Session=Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not Validate Credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    token = verify_token_access(token, credentials_exception)
    try:
        result = crud.deletedata(deleteid=deleteid ,db=db)
        return result
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Not found the data")   
    

@router.put("/update_data{id}")
def update_product(updateid : str , update_data : schema.UpdateProduct, token :str = Depends(oauth2_scheme),db:Session=Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not Validate Credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    token = verify_token_access(token, credentials_exception)
    try:
        result = crud.updatedata(updateid=updateid,update_data=update_data,db=db)
        return result
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Not found the data") 