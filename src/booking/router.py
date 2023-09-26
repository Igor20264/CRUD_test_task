from typing import List
from fastapi import APIRouter, HTTPException
from src.booking.models import Booking, BookingId
from src.user.models import UserId, User, UserReset

client = edgedb.create_async_client()

router = APIRouter(
    prefix="/booking",
    tags=["Booking"]
)

# Операция добавления бронирования для пользователя
@router.post("/", response_model=dict)
async def create_user_booking(booking: Booking):
    if booking.user_id < 0 or len(fetchal(f"SELECT * FROM User WHERE id = '{booking.user_id}'")) == 0:
        raise HTTPException(status_code=401, detail="User not found")
    if booking.comment:
        executes(f"INSERT INTO Booking (user_id, start_time, end_time, comment) VALUES ({booking.user_id}, {booking.start}, {booking.end}, '{booking.comment}');")
    else:
        executes(f"INSERT INTO Booking (user_id, start_time, end_time) VALUES ({booking.user_id}, {booking.start}, {booking.end});")

    return {"booking_id":fetchal(f"SELECT id FROM Booking ORDER BY id DESC LIMIT 1;")[0][0]}  # Возвращаем индекс созданного пользователя


# Операция получения всех бронирований для пользователя
@router.get("/all", response_model=List[list])
async def get_all_user_bookings(user_id: int):
    data = fetchal(f"""
            SELECT *
            FROM Booking
            WHERE user_id == '{user_id}';
            """)
    return data

# Операция удаления бронирования для пользователя
@router.delete("/", response_model=bool)
async def delete_user_booking(user:UserId, booking_id: int):
    if user.id < 0 or len(fetchal(f"SELECT * FROM User WHERE id = '{user.id}'")) == 0:
        raise HTTPException(status_code=401, detail="User not found")

    if booking_id < 0 or len(fetchal(f"SELECT * FROM Booking WHERE id = '{booking_id}'")) == 0:
        raise HTTPException(status_code=401, detail="Booking not found")

    if chekhex(user.password, fetchal(f"SELECT password FROM User WHERE id = '{user.id}'")[0][0]):
        executes(f"DELETE FROM Booking WHERE id = {booking_id}")
        return True
    return False


# Операция обновления бронирования для пользователя
@router.put("/", response_model=bool)
async def update_user_booking(user:UserId, booking: BookingId):
    if user.id < 0 or len(fetchal(f"SELECT * FROM User WHERE id = '{user.id}'")) == 0:
        raise HTTPException(status_code=401, detail="User not found")

    if booking.id < 0 or len(fetchal(f"SELECT * FROM Booking WHERE id = '{booking.id}'")) == 0:
        raise HTTPException(status_code=401, detail="Booking not found")

    if chekhex(user.password, fetchal(f"SELECT password FROM User WHERE id = '{user.id}'")[0][0]):
        if booking.comment:
            executes(f"""
                    UPDATE Booking
                    SET start_time = {booking.start},
                        end_time = {booking.end},
                        comment = '{booking.comment}'
                    WHERE id = {booking.id} AND user_id = {user.id};
                    """)
        else:
            executes(f"""
                    UPDATE Booking
                    SET start_time = {booking.start},
                        end_time = {booking.end}
                    WHERE id = {booking.id} AND user_id = {user.id};
                    """)
        return True
    return False