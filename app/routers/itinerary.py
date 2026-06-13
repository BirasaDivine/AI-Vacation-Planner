from fastapi import APIRouter , HTTPException , Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.itinerary import Itinerary
from app.schemas.itinerary import ItineraryCreate , ItineraryDayResponse , ItineraryResponse
import app.services.itinerary_service as itinerary_service
from typing import List
router=APIRouter(
    prefix="/api",
    tags=["Planner"]
)


@router.get("/itineraries/{trip_id}" , response_model=List[ItineraryDayResponse])
def get_itineraries(trip_id: int , db:Session=Depends(get_db)):
    return itinerary_service.get_itineraries(trip_id, db)

@router.post("/itineraries" , response_model=ItineraryResponse)
def create_itineraries(data:ItineraryCreate , db:Session=Depends(get_db)):
    return itinerary_service.create_itineraries(data.trip_id, db)
        