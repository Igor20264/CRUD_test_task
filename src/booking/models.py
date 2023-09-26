import datetime

from pydantic import BaseModel
from typing import Optional
from uuid import UUID
class Booking(BaseModel):
    start: datetime.datetime
    end: datetime.datetime
    comment: Optional[str] = None

class BookingId(Booking):
    id: UUID