from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from db.database import get_db

from api.MemberAPI import get_member_by_token

from models.BrandModel import Brand
from models.MemberModel import Member

from schemas import BrandSchema

from crud import BrandCRUD

router = APIRouter(
    prefix="/api/brand"
)

@router.get("/list", response_model=list[BrandSchema.Info])
def get_brand_list(db : Session = Depends(get_db)):
    brand_list = BrandCRUD.get_brand_list(db)
    return brand_list

@router.post("/create", response_model= BrandSchema.Info)
def create_brand(new_brand : BrandSchema.CreateRequest, member : Member = Depends(get_member_by_token), db : Session = Depends(get_db)):
    saved_brand = BrandCRUD.create_brand(db = db, member=member , new_brand = new_brand)
    return Brand.to_info(saved_brand)