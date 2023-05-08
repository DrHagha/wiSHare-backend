from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from models import Anniversary, Brand, Friend, Item, Member, Pay, Shipping, ShippingAddress, Wish
from database import SessionLocal, engine

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


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
