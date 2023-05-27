from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base

# 기념일 클래스
class Anniversary(Base):
    __tablename__ = "anniversaries"
    
    id = Column(Integer, primary_key=True, index=True)
    member = Column(Integer, ForeignKey("members.id"))
    date = Column(DateTime, index=True)
    comment = Column(String)
    
    owner = relationship("Member", foreign_keys=[member])
