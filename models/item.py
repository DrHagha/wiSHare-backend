from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

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
    seller_id = Column(Integer, ForeignKey("brands.id"))

    selling_brand = relationship("Brand", back_populates="selling_items")
    i_am_wished = relationship("Wish", back_populates="wished_item")
