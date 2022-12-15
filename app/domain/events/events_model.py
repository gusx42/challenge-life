from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

class Event(Base):
    __tablename__ = "events"
     
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start = Column(String, nullable=False)
    end = Column(String, nullable=False)
    online_event = Column(Boolean, default=True)
    location_addres = Column(String, nullable=False)
    organizer_email = Column(String, nullable=False)
    status = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="users", uselist=False)
    
    def __repr__(self) -> str:
        return f"{self.description}, {self.name}"
        
                     