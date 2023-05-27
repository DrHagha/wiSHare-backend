from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base

#친구관계 클래스
class Friend(Base):
    __tablename__ = "friends"
    
    id = Column(Integer, primary_key=True, index=True)
    caller_id = Column(Integer, ForeignKey("members.id"), index = True)
    receiver_id = Column(Integer, ForeignKey("members.id"), index = True)
    state = Column(String, primary_key = True, index = True)
    
    member1 = relationship("Member", foreign_keys = [caller_id])
    member2 = relationship("Member", foreign_keys = [receiver_id])
    