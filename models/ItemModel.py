from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base

from models import BrandModel

from schemas import ItemSchema

#상품
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    description = Column(String)
    profile_image_path = Column(String)
    price = Column(Integer)
    hit = Column(Integer, index=True)
    is_soldout = Column(Boolean)
    stock = Column(Integer)
    selling_brand_id = Column(Integer, ForeignKey("brands.id"))

    selling_brand = relationship("Brand", foreign_keys=[selling_brand_id])
    
    def to_info(self):
        brand = self.selling_brand
        brand_simple_info = brand.to_simple_info()
        
        response_schema = ItemSchema.Info(
            id = self.id,
            name = self.name,
            price = self.price,
            category= self.category,
            profile_image_path = self.profile_image_path,
            description=self.description,
            hit = self.hit,
            stock = self.stock,
            is_soldout= self.is_soldout,
            selling_brand=brand_simple_info
        )
        return response_schema
    
    def to_info_list(item_list : list['Item']):
        info_list = [Item.to_info(item) for item in item_list]
        return info_list
