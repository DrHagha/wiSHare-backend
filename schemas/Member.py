from typing import Optional

from pydantic import BaseModel, validator

from datetime import datetime

class MemberBase(BaseModel):
    group_id :Optional[int] = None
    id : Optional[str] = None
    pw : Optional[str] = None
    name : Optional[str] = None
    gender : Optional[str] = None
    birthday :Optional[datetime] = None
    profile_image : Optional[str] = None
    reg_date :Optional[datetime] = None
    sec_date :Optional[datetime] = None
    is_use :Optional[bool] = None

class MemberCreate(MemberBase):
    group_id :int
    id : str
    pw1 : str
    pw2 : str
    name : str
    gender : str
    birthday :datetime
    profile_image : str
    reg_date : datetime
    
    @validator('pw2')
    def passwords_match(cls, v, values):
        if 'pw1' in values and v != values['pw1']:
            raise ValueError('비밀번호가 일치하지 않습니다')
        return v

class MemberUpdate(MemberBase):
    group_id :int
    id : str
    pw : str
    name : str
    gender : str
    birthday :datetime
    profile_image : str
    
class MemberInDBBase(MemberBase):
    pk : int
    group_id : int
    id : str
    pw : str
    name : str
    gender : str
    birthday : datetime
    profile_image : str
    reg_date : datetime
    sec_date : Optional[datetime] = None
    is_use : bool
    
    class Config:
        orm_mode = True
        
class Member(MemberInDBBase):
    pass

class MemberInDB(MemberInDBBase):
    pass