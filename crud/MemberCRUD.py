from sqlalchemy.orm import Session
from passlib.context import CryptContext

from models.MemberModel import Member
from schemas import MemberSchema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_member_list(db: Session):
    member_list = db.query(Member)\
        .order_by(Member.id)\
        .all()
    return member_list

def get_by_login_id(db : Session, login_id : str):
    print(login_id)
    member = db.query(Member).filter(Member.login_id == login_id).first()
    print(member)
    return member

def get_detail(db : Session, id : int):
    member = db.query(Member).filter(Member.id == id).first()
    return member

def create_member(db : Session, member : MemberSchema.CreateRequest):
    #추후 겹치는 회원 불가
    db_member = Member(
        group_id = member.group_id,
        login_id = member.login_id,
        password = pwd_context.hash(member.password),
        name = member.name,
        gender = member.gender,
        birthday = member.birthday,
        profile_image_path = "",
        )
    db.add(db_member)
    db.commit()
    return db_member

