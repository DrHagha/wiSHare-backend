from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base

#상품
class Item(Base):
    __tablename__ = "items"

    pk = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    description = Column(String)
    profile_image = Column(String)
    price = Column(Integer)
    hit = Column(Integer, index=True)
    is_soldout = Column(Boolean)
    stock = Column(Integer())
    selling_brand_id = Column(Integer, ForeignKey("brands.pk"))

    selling_brand = relationship("Brand", foreign_keys=[selling_brand_id])
