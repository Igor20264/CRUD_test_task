# 19.09.2023 21:39:45
# Тут был Хлеб

import sqlite3
import time
from logging import log

from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any
from BaseModels import User, Booking, UserId, BookingId  # Базовые модели
from fastapi.openapi.docs import get_swagger_ui_html
import os
import bcrypt
import create_db

app = FastAPI()

def chekhex(data,hash):
    if bcrypt.checkpw(bytes(data, 'utf-8'), bytes(hash, 'utf-8')):
        return True
    return False

def tohex(data:str):
    data = bcrypt.hashpw(bytes(data, 'utf-8'), bcrypt.gensalt()).decode("utf-8")
    return data

# Операция создания пользователя (Create)

# Операция добавления бронирования для пользователя
@app.post("/booking", response_model=dict)
def create_user_booking(booking: Booking):
    if booking.user_id < 0 or len(fetchal(f"SELECT * FROM User WHERE id = '{booking.user_id}'")) == 0:
        raise HTTPException(status_code=401, detail="User not found")
    if booking.comment:
        executes(f"INSERT INTO Booking (user_id, start_time, end_time, comment) VALUES ({booking.user_id}, {booking.start}, {booking.end}, '{booking.comment}');")
    else:
        executes(f"INSERT INTO Booking (user_id, start_time, end_time) VALUES ({booking.user_id}, {booking.start}, {booking.end});")

    return {"booking_id":fetchal(f"SELECT id FROM Booking ORDER BY id DESC LIMIT 1;")[0][0]}  # Возвращаем индекс созданного пользователя


# Операция получения всех бронирований для пользователя
@app.get("/booking/{user_id}/all", response_model=List[list])
def get_all_user_bookings(user_id: int):
    data = fetchal(f"""
            SELECT *
            FROM Booking
            WHERE user_id == '{user_id}';
            """)
    return data

# Операция удаления бронирования для пользователя
@app.delete("/booking/", response_model=bool)
def delete_user_booking(user:UserId, booking_id: int):
    if user.id < 0 or len(fetchal(f"SELECT * FROM User WHERE id = '{user.id}'")) == 0:
        raise HTTPException(status_code=401, detail="User not found")

    if booking_id < 0 or len(fetchal(f"SELECT * FROM Booking WHERE id = '{booking_id}'")) == 0:
        raise HTTPException(status_code=401, detail="Booking not found")

    if chekhex(user.password, fetchal(f"SELECT password FROM User WHERE id = '{user.id}'")[0][0]):
        executes(f"DELETE FROM Booking WHERE id = {booking_id}")
        return True
    return False


# Операция обновления бронирования для пользователя
@app.put("/booking/", response_model=bool)
def update_user_booking(user:UserId, booking: BookingId):
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

@app.on_event("shutdown")
async def shutdown():
    connection.close()
