from fastapi import Depends , HTTPException , APIRouter 
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate , UserResponse
from sqlalchemy.orm import Session
from app.database import get_db
import app.services.auth_service as auth_service

router=APIRouter(
    prefix="/api",
    tags=["Planner"]
)
@router.post("/register" , response_model=UserResponse)
def register(data:UserCreate , db : Session=Depends(get_db)):
    return auth_service.register(data, db)

@router.post("/login")
def login(form_data:OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    return auth_service.login(form_data.username, form_data.password, db)