from pydantic import BaseModel

class TripCreate(BaseModel):
    destination : str
    days : int
    budget : int
    trip_style : str

class TripResponse(BaseModel):
    id : int
    destination : str
    days : int
    budget : int
    trip_style : str
    message : str