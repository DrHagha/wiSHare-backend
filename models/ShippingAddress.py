from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class ShippingAddress(Base):
    __tablename__ = "shipping_addresses"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    zip_code = Column(String)
    user_id = Column(String, ForeignKey("users.id"))

    shipping = relationship("Shipping", back_populates="pay_info")
    owner = relationship("User", back_populates="my_addresses")
