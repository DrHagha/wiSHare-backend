from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from datetime import datetime

from database import Base


class Member(Base):
    __tablename__ = "members"

    pk = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, index=True)
    id = Column(String, index=True)
    pw = Column(String, nullable=False)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    birthday = Column(DateTime, nullable=False)
    profile_image = Column(String, nullable=True)
    reg_date = Column(DateTime, nullable=False, default=datetime.now())
    sec_date = Column(DateTime, nullable=True)
    is_use = Column(Boolean, nullable=False, default=True)

    my_addresses = relationship("ShippingAddress", back_populates="owner")
    my_wish = relationship("Wish", back_populates="wishing_user")
    send_item = relationship("Pay", back_populates="sender")
    recive_item = relationship("Pay", back_populates="reciver")
    my_addresses = relationship("ShippingAddress", back_populates="owner")
    
    i_am_representative = relationship("Brand", back_populates="brand_admin")
    
    friend_caller = relationship("Friend", back_populates = "member1")
    friend_reciver = relationship("Friend", back_populates = "member2")