from sqlalchemy.orm import Session

from models.BrandModel import Brand
from models.MemberModel import Member

from schemas import BrandSchema

def get_brand_list(db : Session):
    brand_list = db.query(Brand).order_by(Brand.id).all()
    brand_info_list = Brand.to_info_list(brand_list=brand_list)
    return brand_info_list

def create_brand(db : Session, member : Member, new_brand : BrandSchema.CreateRequest):
    agent_id = member.id
    db_brand = Brand(
        name = new_brand.name,
        category = new_brand.category,
        description = new_brand.description,
        profile_image_path = new_brand.profile_image_path,
        company_registration_number = new_brand.company_registration_number,
        address = new_brand.address,
        brand_admin_id = agent_id
    )
    
    db.add(db_brand)
    db.commit()
    return Brand.to_info(db_brand)

def get_brand_by_agent(db : Session, agent : Member):
    brand = db.query(Brand).filter(Brand.brand_admin_id == agent.id).first()
    return brand