from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

#결제상태
class Pay(Base):
    __tablename__ = "paies"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))
    sender_id = Column(Integer, ForeignKey("users.id"))
    received_date = Column(DateTime)
    send_date = Column(DateTime)
    shipping_address = Column(String)
    zip_code = Column(String)
    payment_method = Column(String)
    state = Column(String)

    shared_wish_item = relationship("Item", back_populates="paied_item")
    sender = relationship("User", back_populates="send_item")
    reciver = relationship("User", back_populates="recive_item")
