from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from starlette.middleware.cors import CORSMiddleware

from db.database import SessionLocal, engine

from api import MemberAPI, BrandAPI, ItemAPI, FriendAPI

app = FastAPI()

#api import
app.include_router(MemberAPI.router)
app.include_router(BrandAPI.router)
app.include_router(ItemAPI.router)
app.include_router(FriendAPI.router)