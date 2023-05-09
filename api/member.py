from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from starlette import status

from db.database import get_db

from crud import MemberCRUD
from schemas import Member

router = APIRouter(
    prefix="/api/member",
)

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def member_create(_member_create : Member.MemberCreate, db: Session = Depends(get_db)):
    MemberCRUD.create_member(db = db,  member_create=_member_create)
    
@router.get("/read_list", response_model=list[Member.MemberInDBBase])
def member_list_read(db: Session = Depends(get_db)):
    member_list = MemberCRUD.read_member_list(db);
    return member_list