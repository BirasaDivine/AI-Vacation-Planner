from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password, create_access_token

def register(data: UserCreate, db: Session):
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=401, detail="User Already Exists")
    hashed = hash_password(data.password)
    new_user = User(name=data.name, email=data.email, password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login(email: str, password: str, db: Session):
    existing_user = db.query(User).filter(User.email == email).first()
    if not existing_user:
        raise HTTPException(status_code=401, detail="User not found")
    verified = verify_password(password, existing_user.password)
    if not verified:
        raise HTTPException(status_code=401, detail="Password not Verified")
    token = create_access_token({"sub": existing_user.email})
    return {"access_token": token, "token_type": "bearer"}