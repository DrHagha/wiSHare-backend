from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

#결제상태
class Pay(Base):
    __tablename__ = "paies"

    pk = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.pk"))
    receiver_id = Column(Integer, ForeignKey("members.pk"), index = True)
    sender_id = Column(Integer, ForeignKey("members.pk"), index = True)
    received_date = Column(DateTime)
    send_date = Column(DateTime)
    shipping_address_id = Column(Integer, ForeignKey("shipping_addresses.pk"))
    zip_code = Column(String)
    payment_method = Column(String)
    state = Column(String)

    shared_wish_item = relationship("Item", back_populates="paied_item")
    sender = relationship("Memeber", back_populates="send_item")
    reciver = relationship("Memeer", back_populates="recive_item")
    destination = relationship("ShippingAddress", back_populates = "paying_item")
