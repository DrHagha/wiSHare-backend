from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base

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

    brand_admin = relationship("Member", foreign_keys= [agent_id])
