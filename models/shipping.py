from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Shipping(Base):
    __tablename__ = "shipping"

    id = Column(Integer, primary_key=True, index=True)
    pay_id = Column(Integer, ForeignKey("paies.pk"))
    shipper = Column(String)
    state = Column(String)

    pay_info = relationship("Pay", back_populates="shipping")
