from models import AnniversaryModel
from models import BrandModel
from models import FriendModel
from models import ItemModel
from models import MemberModel
from models import PayModel
from models import ShippingModel
from models import ShippingAddressModel
from models import WishModel

alembic_meta_data = [
    AnniversaryModel.Base.metadata,
    BrandModel.Base.metadata,
    FriendModel.Base.metadata,
    ItemModel.Base.metadata,
    MemberModel.Base.metadata,
    PayModel.Base.metadata,
    ShippingAddressModel.Base.metadata,
    ShippingModel.Base.metadata,
    WishModel.Base.metadata
]