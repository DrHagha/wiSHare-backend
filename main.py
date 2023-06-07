from typing import List

from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from starlette.middleware.cors import CORSMiddleware

from db.database import SessionLocal, engine, Base

from api import MemberAPI, BrandAPI, ItemAPI, FriendAPI, AnniversaryAPI, WishAPI, ShippingAddressAPI

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

#api import
app.include_router(MemberAPI.router)
app.include_router(BrandAPI.router)
app.include_router(ItemAPI.router)
app.include_router(FriendAPI.router)
app.include_router(AnniversaryAPI.router)
app.include_router(WishAPI.router)
app.include_router(ShippingAddressAPI.router)