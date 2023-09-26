import uuid
from typing import List

import edgedb.errors
from fastapi import APIRouter, HTTPException
from src.booking.models import Booking, BookingId
from src.user.models import UserId, User, UserReset
import edgedb
from queries import create_booking_async_edgeql as cb
from queries import create_booking_comment_async_edgeql as cbc
from queries import delete_booking_async_edgeql as db
from queries import get_all_booking_async_edgeql as get_all
from queries import get_all_user_booking_async_edgeql as get_all_user
from queries import update_booking_async_edgeql as updatebooking
from src.user.utils import password_cheker

client = edgedb.create_async_client()

router = APIRouter(
    prefix="/booking",
    tags=["Booking"]
)


@router.post("/", response_model=cb.CreateBookingResult)
async def create_user_booking(booking: Booking,user_id: uuid.UUID):
    try:
        if booking.comment:
            s = await cbc.create_booking_comment(client,id=user_id,start=booking.start,end=booking.end,comment=booking.comment)
        else:
            s = await cb.create_booking(client, id=booking.id, start=booking.start, end=booking.end)
        return s
    except edgedb.errors.MissingRequiredError:
        raise HTTPException(status_code=403, detail="User Id is not corrected")

@router.get("/all", response_model=list[get_all.GetAllBookingResult])
async def get_all_user_bookings():
    return await get_all.get_all_booking(client)


@router.get("/", response_model=List[get_all_user.GetAllUserBookingResult])
async def get_all_user_bookings(user_id: uuid.UUID):
    return await get_all_user.get_all_user_booking(client,user_id=user_id)

@router.delete("/", response_model=db.DeleteBookingResult)
async def delete_user_booking(user:UserId, booking_id: uuid.UUID):
    if await password_cheker(client, user.password, uuid.UUID(user.id)):
        return await db.delete_booking(client,id=booking_id, user_id=uuid.UUID(user.id))
    raise HTTPException(status_code=403, detail="Password is not corrected")

# Операция обновления бронирования для пользователя
@router.put("/", response_model=bool)
async def update_user_booking(user:UserId, booking: BookingId):
    if await password_cheker(client, user.password, uuid.UUID(user.id)):
        return await updatebooking.update_booking(client,id=uuid.UUID(booking.id),comment=booking.comment,end=booking.end,start=booking.start)
    raise HTTPException(status_code=403, detail="Password is not corrected")
