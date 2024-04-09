from dotenv import load_dotenv
import os
load_dotenv()


class Settings():
    SECRET_KEY = os.environ.get('SECRET_KEY',None)
    ALGORITHM = os.environ.get('ALGORITHM',None)
    ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES',None)
    REFRESH_TOKEN_EXPIRE_DAYS = os.environ.get('REFRESH_TOKEN_EXPIRE_DAYS',None)
    EMAIL_HOST=os.environ.get('EMAIL_HOST' , None)
    EMAIL_PORT=os.environ.get('EMAIL_PORT' , None)
    EMAIL_USERNAME=os.environ.get('EMAIL_USERNAME' , None)
    EMAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD' ,None)
    EMAIL_FROM=os.environ.get('EMAIL_FROM' , None)


    class Config:
        env_file = './.env'


settings = Settings()
