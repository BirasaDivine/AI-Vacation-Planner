from fastapi import Depends  ,HTTPException
from app.schemas.trip import TripCreate 
from sqlalchemy.orm import Session
from app.models.trip import Trip



def get_all_trips(db:Session):
    trips=db.query(Trip).all()
    return trips


def create_trip(data:TripCreate , db:Session):

    new_trip=Trip( destination=data.destination , days=data.days , budget=data.budget , trip_style=data.trip_style)
    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)
    return new_trip


def get_trip(id: int , db:Session):
    trip=db.query(Trip).filter(Trip.id== id).first()
    if not trip:
        raise HTTPException(status_code=404 , detail="Trip Not Found")
    return trip

def put_trip(id: int , data : TripCreate, db:Session):
    trip=db.query(Trip).filter(Trip.id== id).first()
    if not trip:
        raise HTTPException(status_code=404 , detail="Trip Not Found")
    trip.destination = data.destination # type: ignore
    trip.days = data.days # type: ignore
    trip.budget = data.budget # type: ignore
    trip.trip_style = data.trip_style # type: ignore
    db.commit()
    db.refresh(trip)
    return trip


def delete_trip(id:int , db:Session):
    trip=db.query(Trip).filter(Trip.id== id).first()
    if not trip:
        raise HTTPException(status_code=404 , detail="Trip Not Found")
    
    db.delete(trip)
    db.commit()
    return{ "message" : "Trip deleted"}