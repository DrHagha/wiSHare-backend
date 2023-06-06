from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from db.database import get_db

from api.MemberAPI import get_member_by_token

from crud import AnniversaryCRUD

from schemas import AnniversarySchema

from models import MemberModel

router = APIRouter(
    prefix="/api/annivarsary"
)

@router.get("/list", response_model=list[AnniversarySchema.Info])
def get_anniversary_list(db : Session = Depends(get_db)):
    anniversary_list = AnniversaryCRUD.get_anniversary_list(db = db)
    return anniversary_list

@router.post("/create", response_model=AnniversarySchema.Info)
def create_anniversary(new_anniversary : AnniversarySchema.CreateRequest, member : MemberModel.Member = Depends(get_member_by_token), db : Session = Depends(get_db)):
    saved_anniversary = AnniversaryCRUD.create_anniversary(db = db, member = member, new_anniversary = new_anniversary)
    return saved_anniversary