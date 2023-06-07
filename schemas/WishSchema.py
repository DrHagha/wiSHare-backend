from pydantic import BaseModel
from typing import Optional 

from schemas import MemberSchema, ItemSchema

class Base(BaseModel):
    id : Optional[int] = None
    item_id : Optional[int] = None
    member_id : Optional[int] = None
    is_open : Optional[bool] = None
    
    class Config:
        orm_mode = True
    
class Info(Base):
    id : int
    item_id : int
    member_id : int
    is_open : bool
    member : MemberSchema.Info
    item : ItemSchema.Info
    
class CreateRequest(Base):
    item_id : int