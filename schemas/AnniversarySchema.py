from pydantic import BaseModel
from typing import Optional
import datetime

from schemas import MemberSchema

class Base(BaseModel):
    id : Optional[int] = None
    member_id : Optional[int] = None
    date : Optional[datetime.datetime] = None
    comment : Optional[str] = None
    
    class Config:
        orm_mode = True

class Info(Base):
    id : int
    member_id : int
    date : datetime.datetime
    comment : str
    member : MemberSchema.Info
    
class CreateRequest(Base):
    date : datetime.datetime
    comment : str