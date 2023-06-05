from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from db.database import get_db

from api.MemberAPI import get_member_by_token

from crud import FriendCRUD

from models import MemberModel, FriendModel

from schemas import FriendSchema

router = APIRouter(
    prefix="/api/friend"
)

@router.get("/my_freind_list", response_model=list[FriendSchema.Info])
def get_my_friend_list(db : Session = Depends(get_db), member : MemberModel.Member = Depends(get_member_by_token)):
    friend_list = FriendCRUD.get_my_list(db = db, member = member)
    return friend_list

@router.post("/create", response_model=FriendSchema.Info)
def create_friend(new_freind : FriendSchema.CreateRequest, db : Session = Depends(get_db), member : MemberModel.Member = Depends(get_member_by_token)):
    saved_friend = FriendCRUD.create_friend(db = db, member = member, new_friend = new_freind)
    return saved_friend.to_info()