from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

from db.database import get_db

from datetime import timedelta, datetime

from models.MemberModel import Member
from schemas import MemberSchema
from crud import MemberCRUD

from secret.login_info import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM

router = APIRouter(
    prefix="/api/member",
)

@router.get("/list", response_model=list[MemberSchema.Base])
def get_memberList(db: Session = Depends(get_db)):
    member_list = MemberCRUD.get_member_list(db)
    db.close()
    return member_list

@router.get("/detail/{member_id}", response_model=MemberSchema.Base)
def get_memberList(member_id : int, db: Session = Depends(get_db)):
    member_list = MemberCRUD.get_detail(db, member_id)
    db.close()
    return member_list

@router.post("/create", response_model=MemberSchema.Info)
def create_member(new_member : MemberSchema.CreateRequest, db : Session = Depends(get_db)):
    new_member = MemberCRUD.create_member(db, member = new_member)
    return Member.to_info(new_member)

@router.post("login")
def login(form_data : OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    member = MemberCRUD.get_by_login_id(db = db, login_id=form_data.username)
    if not member or not MemberCRUD.pwd_context.verify(form_data.password, member.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    data = {
        "sub": member.name,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": member.name
    }