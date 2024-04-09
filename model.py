from database import Base
from sqlalchemy import Column,ForeignKey,Integer,String,Boolean,TIMESTAMP,DECIMAL
from sqlalchemy.orm import relationship
import uuid
import datetime




class Business(Base):
    __tablename__ = "business"
    id = Column(String(100),default=uuid.uuid4,primary_key=True,unique=True)
    business_name = Column(String(200),nullable=False)
    city = Column(String(200),nullable=True,default="Unspecified")
    region = Column(String(200),nullable=True,default="Unspecified")
    business_description =Column(String(300),nullable=True)
    logo = Column(String(200),nullable=True)
    owner_id = Column(String(100),ForeignKey('owner.id',ondelete='CASCADE'))
    owners = relationship('Owner')


class Owner(Base):
    __tablename__ = "owner"
    id = Column(String(100),default=uuid.uuid4,primary_key=True,unique=True)
    ownername = Column(String(200),nullable=False)
    email = Column(String(200), nullable=True,unique=True) 
    password = Column(String(200), nullable=True)
    is_verifide = Column(Boolean, nullable=False)
    join_date = Column(TIMESTAMP,default=datetime.datetime.now(),nullable=True)

    
   

class Product(Base):
    __tablename__ = "Product"
    id = Column(String(100),default=uuid.uuid4,primary_key=True,unique=True)
    name = Column(String(200),nullable=True)
    category = Column(String(200),nullable=True)
    original_price = Column(DECIMAL,nullable=True) 
    new_price = Column(DECIMAL,nullable=True)
    percentage_discount = Column(Integer,nullable=True)
    offer_expiration_date = Column(TIMESTAMP,onupdate=datetime.datetime.now(),nullable=True)
    product_image = Column(String(200),nullable=True)
    date_published = Column(TIMESTAMP,default=datetime.datetime.now(),nullable=True) 
    business_id = Column(String(100),ForeignKey("business.id" , ondelete='CASCADE'),nullable=True)
    businesses = relationship('Business')


class User(Base):
    __tablename__ = "users"
    id = Column(String(100),default=uuid.uuid4,primary_key=True,unique=True)
    username = Column(String(200))
    user_email = Column(String(200),unique=True)
    password = Column(String(200))    


        


