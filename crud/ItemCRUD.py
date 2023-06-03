from sqlalchemy.orm import Session

from . import BrandCRUD

from models import ItemModel, MemberModel

from api.MemberAPI import get_member_by_token

from schemas import ItemSchema

def get_item_list(db : Session):
    item_list = db.query(ItemModel.Item).order_by(ItemModel.Item.id).all()
    item_info_list = ItemModel.Item.to_info_list(item_list=item_list)
    return item_info_list

def create_item(db : Session, member : MemberModel.Member, new_item : ItemSchema.CreatRequest):
    brand = BrandCRUD.get_brand_by_agent(db = db, agent = member)
    
    db_item = ItemModel.Item(
        name = new_item.name,
        price = new_item.price,
        category = new_item.category,
        description = new_item.description,
        selling_brand_id = brand.id,
        stock = 0,
        is_soldout = False,
        hit = 0
    )
    
    db.add(db_item)
    db.commit()
    return db_item.to_info()