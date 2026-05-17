from app.database import Base
from sqlalchemy import Column , Integer , String , ForeignKey ,JSON


class Itinerary(Base):
    __tablename__= "itinerary"
    id = Column (Integer ,primary_key=True , nullable= False)
    trip_id = Column (Integer , ForeignKey("trip.id") ,nullable=False , index= True)
    day = Column (Integer , nullable= False)
    activities = Column(JSON , nullable= False)