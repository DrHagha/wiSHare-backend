from fastapi import Depends

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base, get_db

from crud import MemberCRUD

from models import MemberModel
from schemas import BrandSchema

#브랜드 클래스
class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    category = Column(String, index=True)
    description = Column(String)
    profile_image_path = Column(String)
    company_registration_number = Column(String)
    address = Column(String)

    brand_admin_id = Column(Integer, ForeignKey("members.id"))
    brand_admin = relationship("Member", backref="charging_brand")



    def to_info(brand):
        
        member = brand.brand_admin
        
        member_info = MemberModel.Member.to_info(member = member)
        
        response_member = BrandSchema.Info(
            id = brand.id,
            name = brand.name,
            category = brand.category,
            description= brand.description,
            profile_image_path=brand.profile_image_path,
            company_registration_number = brand.company_registration_number,
            address=brand.address,
            brand_admin = member_info
        )
        return response_member
    
    
    def to_info_list(brand_list : list[BrandSchema.Info]):
        info_list = [Brand.to_info(brand) for brand in brand_list]
        return info_list