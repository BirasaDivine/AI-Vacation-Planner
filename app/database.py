from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

engine=create_engine(url="sqlite:///./vacation_planner.db" , connect_args={"check_same_thread" : False})
SessionLocal=sessionmaker(autoflush= False , autocommit=False , bind= engine)
Base= declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()