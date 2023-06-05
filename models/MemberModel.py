from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from datetime import datetime

from db.database import Base

from schemas import MemberSchema


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, index=True)
    login_id = Column(String, index=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    birthday = Column(DateTime, nullable=False)
    profile_image_path = Column(String, nullable=True)
    reg_date = Column(DateTime, nullable=False, default=datetime.now())
    sec_date = Column(DateTime, nullable=True)
    is_use = Column(Boolean, nullable=False, default=True)
    
    
    
    #관계 정의
    def to_info(member):
        group_str = ""
        if member.group_id == 1:
            group_str = "관리자"
        elif member.group_id == 2:
            group_str = "마켓 담당자"
        else:
            group_str = "일반 회원"
        response_member = MemberSchema.Info(
            group_id= member.group_id,
            group=group_str,
            login_id=member.login_id,
            name=member.name,
            gender = member.gender,
            birthday=member.birthday,
            reg_date=member.reg_date
        )
        return response_member
    
