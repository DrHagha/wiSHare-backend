from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from starlette.middleware.cors import CORSMiddleware

from models import Anniversary, Brand, Friend, Item, Member, Pay, Shipping, ShippingAddress, Wish
from db.database import SessionLocal, engine

from api import member, login

Member.Base.metadata.create_all(bind=engine)
Friend.Base.metadata.create_all(bind=engine)
Brand.Base.metadata.create_all(bind=engine)
Item.Base.metadata.create_all(bind=engine)
ShippingAddress.Base.metadata.create_all(bind=engine)
Wish.Base.metadata.create_all(bind=engine)
Shipping.Base.metadata.create_all(bind=engine)
Anniversary.Base.metadata.create_all(bind=engine)
Pay.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(member.router)
app.include_router(login.router)