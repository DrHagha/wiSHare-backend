from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import relationship

from schemas import BrandSchema

class Base(BaseModel):
    id : Optional[int] = None
    name : Optional[str] = None
    price : Optional[int] = None
    category : Optional[str] = None
    profile_image_path : Optional[str] = None
    description : Optional[str] = None
    hit : Optional[int] = None
    stock : Optional[int] = 0
    is_soldout : Optional[bool] = False
    selling_brand_id : Optional[int] = None

    class Config:
        orm = True
        
class CreatRequest(Base):
    name : str
    price : int
    category : str
    description : str
    #나중에 사진 추가 필요
    
class Info(Base):
    id : int
    name : str
    price : int
    category :str
    profile_image_path : Optional[str] = None
    description : str
    hit : int
    stock : int
    is_soldout : bool
    selling_brand : BrandSchema.SimpleInfo