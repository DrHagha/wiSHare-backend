from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from db.database import get_db

from api.MemberAPI import get_member_by_token

from schemas import ItemSchema

from crud import ItemCRUD

from models import MemberModel

router = APIRouter(
    prefix="/api/item"
)

@router.get("/list", response_model=list[ItemSchema.Info])
def get_list(db : Session = Depends(get_db)):
    item_list = ItemCRUD.get_item_list(db)
    return item_list


@router.post("/create", response_model=ItemSchema.Info)
def create_item(new_item : ItemSchema.CreatRequest, member : MemberModel.Member = Depends(get_member_by_token), db : Session = Depends(get_db)):
    saved_item = ItemCRUD.create_item(db = db, member = member, new_item = new_item)
    return saved_item