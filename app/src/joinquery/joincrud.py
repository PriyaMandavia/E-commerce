from app.src.joinquery import joinschema
import model
from sqlalchemy.orm import Session,joinedload
from fastapi.encoders import jsonable_encoder






def details(name : str ,limit :int,page :int , db:Session):
        offset = (page-1)*limit

        search = db.query(model.Business.business_name,
                          model.Business.business_description,
                          model.Business.city,
                          model.Owner.ownername,
                          model.Owner.is_verifide).join(model.Owner).filter(model.Business.business_name.like(f"{name}%")).limit(limit).offset(offset).all()
        
        total = db.query(model.Business.business_name,
                          model.Business.business_description,
                          model.Business.city,
                          model.Owner.ownername,
                          model.Owner.is_verifide).join(model.Owner).filter(model.Business.business_name.like(f"{name}%")).count()
       
        search_data =[]
    

        for data in search:
            
            search_item = joinschema.Show( business_name = data.business_name,
                                                        business_description = data.business_description,
                                                        city=data.city,
                                                        ownername=data.ownername,
                                                        is_verifide=data.is_verifide)
            search_data.append(search_item)
        return jsonable_encoder(search_data) , total



def show_data(name : str ,limit :int,page : int, db:Session):
      
        offset = (page-1) * limit

        query = db.query(model.Business.business_name,model.Owner.ownername,
                        model.Business.city,model.Product.category,
                        model.Product.offer_expiration_date,model.Product.new_price,
                        model.Product.original_price,model.Product.percentage_discount).join(model.Owner).join(model.Product).filter(model.Business.business_name.like(f"{name}%")).limit(limit).offset(offset).all()
        
        total  = db.query(model.Business.business_name,model.Owner.ownername,
                        model.Business.city,model.Product.category,
                        model.Product.offer_expiration_date,model.Product.new_price,
                        model.Product.original_price,model.Product.percentage_discount).join(model.Owner).join(model.Product).filter(model.Business.business_name.like(f"{name}%")).count()
        
        data = []
        for d in query:
                new_data = joinschema.Show_data(business_name = d.business_name,
                                                ownername = d.ownername,
                                                city = d.city,
                                                category = d.category,
                                                original_price = d.original_price,
                                                new_price = d.new_price,
                                                percentage_discount =d.percentage_discount,
                                                offer_expiration_date = d.offer_expiration_date )
                

                data.append(new_data)
        return jsonable_encoder(data), total                 

