from sqlalchemy.orm import Session

from models import ShippingAddressModel, MemberModel
from schemas import ShippingAddressSchema

def get_shipping_address_list(db : Session):
    shipping_address_list = db.query(ShippingAddressModel.ShippingAddress).order_by(ShippingAddressModel.ShippingAddress.id).all()
    return ShippingAddressModel.ShippingAddress.to_info_list(shipping_address_list=shipping_address_list)

def create_shipping_address(db : Session, member : MemberModel.Member, new_shipping_address : ShippingAddressSchema.CreateRequest):
    db_shipping_address = ShippingAddressModel.ShippingAddress(
        member_id = member.id,
        name = new_shipping_address.name,
        address = new_shipping_address.address,
        zip_code = new_shipping_address.zip_code,
    )
    db.add(db_shipping_address)
    db.commit()
    return db_shipping_address.to_info()