from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

# 기념일 클래스
class Anniversary(Base):
    pk = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey("users.pk"))
    date = Column(DateTime, index=True)
    comment = Column(String)
    
    owner = relationship("Memeber", back_populates="anniversaries")
