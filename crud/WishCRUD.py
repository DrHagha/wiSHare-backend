from sqlalchemy.orm import Session

from models import WishModel, MemberModel
from schemas import WishSchema

def get_wish_list(db : Session):
    wish_list = db.query(WishModel.Wish).order_by(WishModel.Wish.id).all()
    return WishModel.Wish.to_info_list(wish_list)

def create_wish(member : MemberModel.Member, new_wish : WishSchema.CreateRequest, db : Session):
    db_wish = WishModel.Wish(
        item_id = new_wish.item_id,
        member_id = member.id,
        is_open = False
    )
    db.add(db_wish)
    db.commit()
    return db_wish.to_info()