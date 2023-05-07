from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

#친구관계 클래스
class Friend(Base):
    __tablename__ = "friends"
    
    pk = Column(Integer, primary_key=True, index=True)
    caller_id = Column(Integer, ForeignKey("members.pk"), index = True)
    receiver_id = Column(Integer, ForeignKey("members.pk"), index = True)
    state = Column(String, primary_key = True, index = True)
    
    member1 = relationship("Member", back_populates = "friend_caller")
    member2 = relationship("Member", back_populates = "friend_reciver")
    