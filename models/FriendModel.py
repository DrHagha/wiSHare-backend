from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base

from schemas import FriendSchema

from models import MemberModel

#친구관계 클래스
class Friend(Base):
    __tablename__ = "friends"
    
    id = Column(Integer, primary_key=True, index=True)
    
    
    state = Column(String, index = True)
    
    caller_id = Column(Integer, ForeignKey("members.id"), index = True, autoincrement=True)
    caller = relationship("Member", foreign_keys = [caller_id])
    receiver_id = Column(Integer, ForeignKey("members.id"), index = True)
    receiver = relationship("Member", foreign_keys = [receiver_id])
    
    def to_info(self):
        caller = self.caller
        receiver = self.receiver
        
        caller_info = MemberModel.Member.to_info(caller)
        receiver_info = MemberModel.Member.to_info(receiver)
        
        response_friend = FriendSchema.Info(
            id = self.id,
            caller_id= self.caller_id,
            caller= caller_info,
            receiver= receiver_info,
            state= self.state
        )
        return response_friend
    
    def to_info_list(friend_list : list['Friend']):
        info_list = [friend.to_info() for friend in friend_list]
        return info_list