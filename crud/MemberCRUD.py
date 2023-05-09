from sqlalchemy.orm import Session

from datetime import datetime

from schemas.Member import MemberCreate, MemberUpdate
from models.Member import Member as MemberModel

def create_member(db: Session, member_create : MemberCreate):
    db_member = MemberModel(
        group_id = member_create.group_id,
        id = member_create.id,
        pw = member_create.pw,
        name = member_create.name,
        gender = member_create.gender,
        birthday = member_create.birthday,
        profile_image = member_create.profile_image,
        reg_date = datetime.now()
    )
    db.add(db_member)
    db.commit()
    
def read_member_list(db: Session):
    member_list = db.query(MemberModel).order_by(MemberModel.reg_date.desc()).all()
    return member_list