from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base

from schemas import ShippingAddressSchema, MemberSchema

from models import MemberModel

class ShippingAddress(Base):
    __tablename__ = "shipping_addresses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    zip_code = Column(String)
    member_id = Column(String, ForeignKey("members.id"))

    owner = relationship("Member", foreign_keys=[member_id])

    def to_info(self):
        response_shippingaddress = ShippingAddressSchema.Info(
            id = self.id,
            name= self.name,
            address= self.address,
            zip_code= self.zip_code,
            member_id= self.member_id,
            member = MemberModel.Member.to_info(self.owner)
        )
        return response_shippingaddress
        
    def to_info_list(shipping_address_list : list['ShippingAddress']):
        response_shipping_address_list = [shipping_address.to_info() for shipping_address in shipping_address_list]
        
        return response_shipping_address_list