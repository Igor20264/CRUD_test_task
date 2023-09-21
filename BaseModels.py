
from pydantic import BaseModel
from datetime import datetime
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
    start: datetime
    duration: int
    comment: Optional[str] = None