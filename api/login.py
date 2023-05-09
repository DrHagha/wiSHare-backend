from typing import Annotated

from fastapi import FastAPI, APIRouter, HTTPException, Depends

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from crud.LoginCRUD import get_current_member, fake_members_db, fake_hash_password, get_current_active_member

from schemas.Member import MemberFake

router = APIRouter(
    prefix="/api/login",
)

@router.get("/members/me")
async def read_members_me(current_member: Annotated[MemberFake, Depends(get_current_member)]):
    return current_member

@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    print("hello")
    user_dict = fake_members_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    member = MemberFake(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == member.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": member.name, "token_type": "bearer"}

@router.get("/users/me")
async def read_users_me(
    current_user: Annotated[MemberFake, Depends(get_current_active_member)]
):
    return current_user