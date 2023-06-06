from sqlalchemy.orm import Session

from models import AnniversaryModel, MemberModel

from schemas import AnniversarySchema

def get_anniversary_list(db : Session):
    anniversary_list = db.query(AnniversaryModel.Anniversary).order_by(AnniversaryModel.Anniversary.id).all()
    return AnniversaryModel.Anniversary.to_info_list(anniversary_list=anniversary_list)

def create_anniversary(db : Session, member : MemberModel.Member, new_anniversary : AnniversarySchema.CreateRequest):
    db_anniversary = AnniversaryModel.Anniversary(
        member_id = member.id,
        date = new_anniversary.date,
        comment = new_anniversary.comment
    )
    db.add(db_anniversary)
    db.commit()
    return db_anniversary.to_info()