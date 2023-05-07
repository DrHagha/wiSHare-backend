from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

#브랜드 클래스
class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey("user.id"))
    name = Column(String, unique=True, index=True)
    category = Column(String, index=True)
    description = Column(String)
    profile_image = Column(String)
    company_registration_number = Column(String)
    agent = Column(String)
    address = Column(String)

    selling_items = relationship("Item", back_populates="seller")
    representative = relationship("User", back_populates="i_am_representative")
