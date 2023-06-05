from sqlalchemy.orm import Session

from models import MemberModel, FriendModel

from schemas import FriendSchema

def get_my_list(db : Session, member : MemberModel.Member):
    friend_list1 = db.query(FriendModel.Friend).filter(FriendModel.Friend.caller_id == member.id).all()
    friend_list2 = db.query(FriendModel.Friend).filter(FriendModel.Friend.receiver_id == member.id).all()
    
    return FriendModel.Friend.to_info_list(friend_list1 + friend_list2)

def create_friend(db : Session, member : MemberModel.Member, new_friend = FriendSchema.CreateRequest):
    new_friend = FriendModel.Friend(
        caller_id = member.id,
        receiver_id = new_friend.receiver_id,
        state = "친구신청"
    )
    db.add(new_friend)
    db.commit()
    return new_friend.to_info()