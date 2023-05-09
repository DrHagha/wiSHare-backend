from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base

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

    shared_wish_item = relationship("Item", foreign_keys=[item_id])
    sender = relationship("Member", foreign_keys=[sender_id])
    reciver = relationship("Member", foreign_keys=[receiver_id])
    destination = relationship("ShippingAddress", foreign_keys = [shipping_address_id])
