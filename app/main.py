from fastapi import FastAPI
from app.database import Base , engine
from app.routers.auth import router as auth_router
from app.routers.trips import router as trips_router
from app.routers.itinerary import router as itinerary_router
app=FastAPI(title= "AI Vacation Planner API")

Base.metadata.create_all(bind=engine)
app.include_router(auth_router)
app.include_router(trips_router)
app.include_router(itinerary_router)
@app.get("/")
def root():
    return {"message": "AI Vacation Planner API is running"}