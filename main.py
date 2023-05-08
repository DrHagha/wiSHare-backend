from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from starlette.middleware.cors import CORSMiddleware

from models import Anniversary, Brand, Friend, Item, Member, Pay, Shipping, ShippingAddress, Wish
from database import SessionLocal, engine

from fastapi.encoders import jsonable_encoder
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

from routes import MemberRouter

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

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Your App Name",
        version="0.1.0",
        description="Your App Description",
        routes=app.routes,
    )
    # Convert Pydantic models to serializable dictionaries
    json_schema = jsonable_encoder(openapi_schema)
    app.openapi_schema = json_schema
    return app.openapi_schema

app.openapi = custom_openapi

app.include_router(MemberRouter.router)