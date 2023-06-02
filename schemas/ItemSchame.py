from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import relationship

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
    selling_brand_id :int