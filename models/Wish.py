from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Wish(Base):
    __tablename__ = "wishes"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.pk"))
    user_id = Column(Integer, ForeignKey("members.pk"))
    is_open = Column(Boolean)

    wished_item = relationship("Item", back_populates="i_am_wished")
    wishing_user = relationship("Member", back_populates="my_wish")
