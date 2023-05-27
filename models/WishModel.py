from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base


class Wish(Base):
    __tablename__ = "wishes"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    member_id = Column(Integer, ForeignKey("members.id"))
    is_open = Column(Boolean)

    wished_item = relationship("Item", foreign_keys=[item_id])
    wishing_user = relationship("Member", foreign_keys=[member_id])
