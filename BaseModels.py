
from pydantic import BaseModel
from typing import Optional

# Модель данных пользователя
class User(BaseModel):
    name: str
    password: str

class Iser(BaseModel): #Как юзер только с id
    id:int
    password:str

# Модель данных бронирования
class Booking(BaseModel):
    user_id:int
    start: int
    end: int
    comment: Optional[str] = None

class Booking_Id(BaseModel):
    id:int
    user_id:int
    start: int
    end: int
    comment: Optional[str] = None
