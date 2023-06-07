from pydantic import BaseModel
from typing import Optional

from schemas import MemberSchema

class Base(BaseModel):
    id : Optional[int] = None
    name : Optional[str] = None
    address : Optional[str] = None
    zip_code : Optional[str] = None
    member_id : Optional[int] = None
    
class Info(Base):
    id : int
    name : str
    address : str
    zip_code : str
    member_id : int
    member : MemberSchema.Info

class CreateRequest(Base):
    name : str
    address : str
    zip_code : str