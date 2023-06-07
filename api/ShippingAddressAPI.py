from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from api.MemberAPI import get_member_by_token

from models import MemberModel

from schemas import ShippingAddressSchema

from crud import ShippingAddressCRUD

router = APIRouter(
    prefix="/api/shipping_address"
)

@router.get("/list", response_model=list[ShippingAddressSchema.Info])
def get_shipping_address_list(db : Session = Depends(get_db)):
    shipping_adress_list = ShippingAddressCRUD.get_shipping_address_list(db = db)
    return shipping_adress_list

@router.post("/create", response_model=ShippingAddressSchema.Info)
def create_shipping_address(new_shipping_address : ShippingAddressSchema.CreateRequest, member : MemberModel.Member = Depends(get_member_by_token), db : Session = Depends(get_db)):
    saved_shipping_address = ShippingAddressCRUD.create_shipping_address(db = db, member = member, new_shipping_address = new_shipping_address)
    return saved_shipping_address