
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.itinerary import Itinerary
from app.schemas.itinerary import ItineraryCreate , ItineraryDayResponse , ItineraryResponse
from app.schemas.trip import TripCreate , TripResponse
from app.models.trip import Trip
from app.claude import add_user_message , chat
import json

def get_itineraries(trip_id: int , db:Session):
    trip=db.query(Itinerary).filter(Itinerary.trip_id == trip_id).all()
    return trip


def prompt(trip_id : int , db:Session):
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404 , detail="Trip Not Found")
    destination=trip.destination
    days=trip.days
    budget=trip.budget
    lifestyle=trip.trip_style
    prompt = f"""
        Plan a {days}-day trip to {destination} with a budget of ${budget}.
        The travel style is {lifestyle}.
        Only suggest places within {destination}.
        Stay within the budget of ${budget} total.

        Return ONLY a JSON array with no extra text, no explanation, no markdown.
        Use exactly this format:
        [
        {{"day": 1, "activities": ["activity1", "activity2", "activity3"]}},
        {{"day": 2, "activities": ["activity1", "activity2", "activity3"]}}
        ]
        Generate exactly {days} days.
        """
    messages=[]
    add_user_message(messages , prompt)
    answer=chat(messages)
    itinerary=json.loads(answer)
    return itinerary

def create_itineraries( trip_id : int, db:Session):
    itinerary=prompt(trip_id ,db)
    for day in itinerary:
        new_entry=Itinerary(
            trip_id = trip_id ,
            day=day["day"],
            activities=day["activities"]
        )
        db.add(new_entry)
    db.commit()
    return {
    "trip_id": trip_id,
    "itinerary": itinerary,
    "message": "Itinerary created successfully"
}
