
from pydantic import BaseModel
from typing import Optional

# Модель данных пользователя
class User(BaseModel):
    name: str
    password: str

class UserId(User): #Как юзер только с id
    id:int
    password:str

class DataUser(UserId):
    id: int
    name: str

# Модель данных бронирования
class Booking(BaseModel):
    user_id:int
    start: int
    end: int
    comment: Optional[str] = None

class BookingId(Booking):
    id:int
    user_id:int
    start: int
    end: int
    comment: Optional[str] = None
