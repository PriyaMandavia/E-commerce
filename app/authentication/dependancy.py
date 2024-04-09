from fastapi.security import OAuth2PasswordBearer
from app.authentication import schema
from datetime import datetime,timedelta 
from jose import JWTError, jwt
from config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')





def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"expire": expire.strftime("%Y-%m-%d %H:%M:%S")})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_token_access(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = schema.DataToken(id=id)
        return token_data
    except JWTError as e:
        print(e)
        raise credentials_exception
    
