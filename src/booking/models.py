import datetime

from pydantic import BaseModel
from typing import Optional
import uuid
class Booking(BaseModel):
    start: datetime.datetime
    end: datetime.datetime
    comment: Optional[str] = None

class BookingId(Booking):
    id: str