
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Модель данных пользователя
class User(BaseModel):
    name: str
    password: str

# Модель данных бронирования
class Booking(BaseModel):
    start: datetime
    duration: int
    comment: Optional[str] = None
