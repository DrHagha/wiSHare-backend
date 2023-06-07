from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base

from schemas import WishSchema


class Wish(Base):
    __tablename__ = "wishes"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    member_id = Column(Integer, ForeignKey("members.id"))
    is_open = Column(Boolean)

    wished_item = relationship("Item", foreign_keys=[item_id])
    wishing_user = relationship("Member", foreign_keys=[member_id])
    
    def to_info(self):
        response_wish = WishSchema.Info(
            id = self.id,
            item_id=self.item_id,
            member_id= self.member_id,
            member= self.wishing_user.to_info(),
            item=self.wished_item.to_info(),
            is_open=self.is_open
        )
        return response_wish
    
    def to_info_list(wish_list : list['Wish']):
        wish_list = [wish.to_info() for wish in wish_list]
        return wish_list
