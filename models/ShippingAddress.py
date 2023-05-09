from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base


class ShippingAddress(Base):
    __tablename__ = "shipping_addresses"

    pk = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    zip_code = Column(String)
    member_id = Column(String, ForeignKey("members.pk"))

    owner = relationship("Member", foreign_keys=[member_id])
