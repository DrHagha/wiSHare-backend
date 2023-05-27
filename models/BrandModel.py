from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base

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
