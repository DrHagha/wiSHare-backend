from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

#브랜드 클래스
class Brand(Base):
    __tablename__ = "brands"

    pk = Column(Integer, primary_key=True, index=True)
    agent_id = Column(Integer, ForeignKey("members.pk"))
    name = Column(String, unique=True, index=True)
    category = Column(String, index=True)
    description = Column(String)
    profile_image = Column(String)
    company_registration_number = Column(String)
    address = Column(String)

    selling_items = relationship("Item", back_populates="selling_brand")
    brand_admin = relationship("Member", back_populates="i_am_representative")
