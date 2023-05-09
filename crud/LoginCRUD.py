from typing import Annotated, Union

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from datetime import datetime

from schemas.Member import MemberFake

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


fake_members_db = {
    "johndoe": {
        "id" : "ddfd",
        "group_id" : 0,
        "name": "johndoe",
        "gender" : "male",
        "birthday": datetime.now(),
        "reg_date ": datetime.now(),
        "sec_date ": datetime.now(),
        "profile_image" : "nono",
        "pw": "fakehashedsecret",
        "disabled": False,
    },
    "eeere": {
        "id" : "ddfd",
        "group_id" : 0,
        "name": "eeere",
        "gender" : "male",
        "birthday": datetime.now(),
        "reg_date ": datetime.now(),
        "sec_date ": datetime.now(),
        "profile_image" : "nono",
        "pw": "fakehashedsecret",
        "disabled": False,
    },
}

def fake_hash_password(password : str):
    return "fakehashed" + password

def get_member_fake(db, member_name : str):
    if member_name in db:
        member_dict = db[member_name]
        return MemberFake(**member_dict)

def fake_decode_token(token):
    member = get_member_fake(fake_members_db, token)
    return member

async def get_current_member(token: Annotated[str, Depends(oauth2_scheme)]):
    member = fake_decode_token(token)
    if not member:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return member

async def get_current_active_member(current_member: Annotated[MemberFake, Depends(get_current_member)]):
    if current_member.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_member