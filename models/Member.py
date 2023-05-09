from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from datetime import datetime

from db.database import Base


class Member(Base):
    __tablename__ = "members"

    pk = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, index=True)
    id = Column(String, index=True)
    pw = Column(String, nullable=False)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    birthday = Column(DateTime, nullable=False)
    profile_image = Column(String, nullable=True)
    reg_date = Column(DateTime, nullable=False, default=datetime.now())
    sec_date = Column(DateTime, nullable=True)
    is_use = Column(Boolean, nullable=False, default=True)