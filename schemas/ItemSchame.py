from pydantic import BaseModel
from sqlalchemy.orm import relationship

class ItemSchema(BaseModel):
    pk : int
    name : str
    price : str
    category : str
    description : str
    hit : int
    stock : int
    is_soldout : bool

    class Config:
        orm = True