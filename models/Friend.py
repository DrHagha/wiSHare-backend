from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

#친구관계 클래스
class Friend(Base):
    __tablename__ = "friend"
    
    pk = Column(Integer, primary_key=True, index=True)
    caller_id = Column(Integer, primary_key = True, index = True)
    receiver_id = Column(Integer, primary_key = True, index = True)
    state = Column(String, primary_key = True, index = True)
    