from pydantic import BaseModel, validator
from typing import Optional
import datetime

class Base(BaseModel):
    id : Optional[int] = None
    group_id : Optional[int] = None
    login_id : Optional[str] = None
    password : Optional[str] = None
    name : Optional[str] = None
    gender : Optional[str] = None
    birthday : Optional[datetime.datetime] = None
    profile_image_path : Optional[str] = None
    reg_date : Optional[datetime.datetime] = None
    sec_date : Optional[datetime.datetime] = None
    is_use : bool = True
    
    class Config:
        orm_mode = True
        
class CreateRequest(Base):
    login_id : str
    group_id : int
    password : str
    password2 : str
    birthday : datetime.datetime
    name : str
    gender : str
    
    @validator('name', 'password', 'password2', 'login_id', 'gender')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    @validator('password2')
    def passwords_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('비밀번호가 일치하지 않습니다')
        return v

class Info(Base):
    group_id : int
    group : str
    login_id : str
    name : str
    gender : str
    birthday : datetime.datetime
    reg_date : datetime.datetime
    
class Token(Base):
    access_token : str
    token_type : str
    name : str