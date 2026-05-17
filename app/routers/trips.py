from fastapi import Depends , APIRouter 
from app.schemas.trip import TripCreate , TripResponse
from sqlalchemy.orm import Session
from app.database import get_db
from typing import List
import app.services.trip_service as trip_service
router=APIRouter(
    prefix="/api",
    tags=["Planner"]
)
@router.get("/trips" , response_model=List[TripResponse])
def get_all_trips(db:Session=Depends(get_db)):
    return trip_service.get_all_trips(db)

@router.post("/trips" , response_model=TripResponse)
def create_trip(data:TripCreate , db:Session=Depends(get_db)):
    return trip_service.create_trip(data,db)

@router.get("/trips/{id}" , response_model=TripResponse)
def get_trip(id: int , db:Session=Depends(get_db)):
    return trip_service.get_trip(id,db)

@router.put("/trips/{id}" , response_model=TripResponse)
def put_trip(id: int , data : TripCreate, db:Session=Depends(get_db)):
    return trip_service.put_trip(id,data,db)

@router.delete("/trips/{id}")
def delete_trip(id:int , db:Session=Depends(get_db)):
    return trip_service.delete_trip(id,db)