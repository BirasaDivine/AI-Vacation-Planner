from pydantic import BaseModel
from typing import List


class ItineraryDay(BaseModel):
    day : int
    activities : list[str]

class ItineraryCreate(BaseModel):
    trip_id : int
    days : List[ItineraryDay]

class ItineraryResponse(BaseModel):
    trip_id : int
    itinerary : List[ItineraryDay]
    message : str

class ItineraryDayResponse(BaseModel):
    id: int
    trip_id: int
    day: int
    activities: List[str]

    class Config:
        from_attributes = True