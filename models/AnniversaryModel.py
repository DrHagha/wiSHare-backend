from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base

from models import MemberModel

from schemas import AnniversarySchema

# 기념일 클래스
class Anniversary(Base):
    __tablename__ = "anniversaries"
    
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey("members.id"))
    date = Column(DateTime, index=True)
    comment = Column(String)
    
    owner = relationship("Member", foreign_keys=[member_id])
    
    def to_info(self):
        member = self.owner
        member_info = MemberModel.Member.to_info(member = member)
        
        response_anniversary = AnniversarySchema.Info(
            id = self.id,
            member_id=self.member_id,
            date= self.date,
            comment= self.comment,
            member = member_info
        )
        return response_anniversary

    def to_info_list(anniversary_list : list['Anniversary']):
        info_list = [anniversary.to_info() for anniversary in anniversary_list]
        return info_list