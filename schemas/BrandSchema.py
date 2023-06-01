from pydantic import BaseModel, validator
from typing import Optional
from schemas import MemberSchema
import datetime

class Base(BaseModel):
    id : Optional[int] = None
    name : Optional[str] = None
    category : Optional[str] = None
    description : Optional[str] = None
    profile_image_path : Optional[str] = None
    company_registration_number : Optional[str] = None
    address : Optional[str] = None
    brand_admin_id : Optional[int] = None
    
    class Config:
        orm_mode = True
        
class Info(Base):
    id : int
    name : str
    category : str
    description : str
    company_registration_number = str
    address = str
    brand_admin : MemberSchema.Info
    
class SimpleInfo(Base):
    pass
    
class CreateRequest(Base):
    name : str
    category : str
    description : str
    company_registration_number : str
    address : str