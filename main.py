from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from starlette.middleware.cors import CORSMiddleware

from models import AnniversaryModel, BrandModel, FriendModel, ItemModel, MemberModel, PayModel, Shipping_model, ShippingAddressModel, WishModel
from db.database import SessionLocal, engine

from api import MemberAPI


MemberModel.Base.metadata.create_all(bind=engine)
FriendModel.Base.metadata.create_all(bind=engine)
BrandModel.Base.metadata.create_all(bind=engine)
ItemModel.Base.metadata.create_all(bind=engine)
ShippingAddressModel.Base.metadata.create_all(bind=engine)
WishModel.Base.metadata.create_all(bind=engine)
Shipping_model.Base.metadata.create_all(bind=engine)
AnniversaryModel.Base.metadata.create_all(bind=engine)
PayModel.Base.metadata.create_all(bind=engine)

app = FastAPI()

#api import
app.include_router(MemberAPI.router)