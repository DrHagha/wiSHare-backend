from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    pk = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, index=True)
    id = Column(String, index=True)
    pw = Column(String)
    name = Column(String)
    gender = Column(String)
    birthday = Column(DateTime)
    profile_image = Column(String)

    my_addresses = relationship("ShippingAddress", back_populates="owner")
    my_wish = relationship("Wish", back_populates="wishing_user")
    send_item = relationship("Pay", back_populates="sender")
    recive_item = relationship("Pay", back_populates="reciver")
    my_addresses = relationship("ShippingAddress", back_populates="owner")
