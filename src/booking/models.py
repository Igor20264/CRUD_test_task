from pydantic import BaseModel
from typing import Optional

class Booking(BaseModel):
    user_id:int
    start: int
    end: int
    comment: Optional[str] = None

class BookingId(Booking):
    id:int