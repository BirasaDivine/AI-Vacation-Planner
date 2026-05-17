from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    name : str
    email : str
    password : str

class UserResponse(BaseModel):
    name : str 
    email : str