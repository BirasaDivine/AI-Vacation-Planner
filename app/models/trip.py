from app.database import Base
from sqlalchemy import Column , Integer , String , ForeignKey


class Trip(Base):
    __tablename__= "trip"
    user_id = Column (Integer , ForeignKey("users.id"), nullable= False , index=True)
    id = Column (Integer , primary_key= True , index=True)
    destination = Column(String(100) , nullable= False) 
    days = Column(Integer , nullable= False) 
    budget =Column(Integer , nullable= False) 
    trip_style = Column(String(100) , nullable= False) 