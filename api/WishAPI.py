from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db

from models import MemberModel
from api.MemberAPI import get_member_by_token

from crud import WishCRUD
from schemas import WishSchema


router = APIRouter(
    prefix="/api/wish"
)

@router.get("/list", response_model=list[WishSchema.Info])
def get_wish_list(db : Session = Depends(get_db)):
    wish_list = WishCRUD.get_wish_list(db = db)
    return wish_list

@router.post("/create", response_model=WishSchema.Info)
def create_wish(new_wish : WishSchema.CreateRequest, member : MemberModel.Member = Depends(get_member_by_token), db : Session = Depends(get_db)):
    saved_wish = WishCRUD.create_wish(db = db, member = member, new_wish = new_wish)
    return saved_wish