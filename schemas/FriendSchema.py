from pydantic import BaseModel
from typing import Optional

from schemas import MemberSchema

class Base(BaseModel):
    id : Optional[int] = None
    caller_id : Optional[int] = None
    receiver_id : Optional[int] = None
    state : Optional[str] = None
    
    class Config:
        orm_mode = True
        
class Info(Base):
    id : int
    caller_id : int
    caller : MemberSchema.Info
    receiver_id : int
    receiver : MemberSchema.Info
    state : str
    
class CreateRequest(Base):
    receiver_id : int
    