
from sqlalchemy.orm import Session
from app.models.itinerary import Itinerary
from app.schemas.itinerary import ItineraryCreate , ItineraryDayResponse , ItineraryResponse



def get_itineraries(trip_id: int , db:Session):
    trip=db.query(Itinerary).filter(Itinerary.trip_id == trip_id).all()
    return trip

def create_itineraries(data:ItineraryCreate , db:Session):
    for day in data.days:
        new_entry=Itinerary( trip_id = data.trip_id , day= day.day , activities=day.activities)
        db.add(new_entry)
    db.commit()
    return {
    "trip_id": data.trip_id,
    "itinerary": data.days,
    "message": "Itinerary created successfully"
}
        