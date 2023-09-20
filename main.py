# 19.09.2023 21:39:45
# Я Хлеб или же Игорь
# Хз зачем ты читаешь это... Ты думаешь тут будет важная информация... Возможно...
# Это стартовый файл, обычно тут ничего нет... Ищи в других файлах!

import sqlite3
import time

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from src.BaseModels import User, Booking, Iser  # Базовые модели
import json
app = FastAPI()

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect('database.db', check_same_thread=False)

def executes(text):
    cursor = connection.cursor()
    cursor.execute(text)
    connection.commit()
    return True

def fetchal(text):
    cursor = connection.cursor()
    cursor.execute(text)
    results = cursor.fetchall()
    return results

users = []

# Операция создания пользователя (Create)
@app.post("/user/add", response_model=int)
def create_user(user: User)->int:
        if len(fetchal(f"SELECT * FROM User WHERE username = '{user.name}'"))==0:
            executes(f"INSERT INTO User (username, password, created, updated) VALUES ('{user.name}', '{user.password}', {time.time()}, {time.time()});")
            return fetchal(f"SELECT * FROM User ORDER BY id DESC LIMIT 1;")[0][0]  # Возвращаем индекс созданного пользователя
        else:
            raise HTTPException(status_code=409, detail="User already exists")

# Операция проверки занятости имени пользователя (Read)
@app.post("/user/checkname", response_model=bool)
def check_username(username: str)->bool:
    if len(fetchal(f"""
    SELECT *
    FROM User
    WHERE username = '{username}'
    """))==0:
        return True
    else:
        raise HTTPException(status_code=409, detail="User already exists")

# Операция получения имени и id пользователя (Read)
@app.post("/user/getname", response_model=int)
def get_user_id_by_name(username: str):
    try:
        id = fetchal(f"""
        SELECT *
        FROM User
        WHERE username = '{username}'
        LIMIT 1;
        """)[0][0]
        return id
    except:
        raise HTTPException(status_code=401, detail="User not found")

# Операция получения всех пользователей (Read All)
@app.get("/user/getall", response_model=List[tuple])
def get_all_users():
    return fetchal(f"""
        SELECT username,id
        FROM User;
        """)

# Операция удаления пользователя (Delete) Хз можно ли, так делать... Но это удаление...
@app.delete("/user/{user_id}/{password}/del", response_model=bool)
def delete_user(user_id:int,password: str):
    if user_id < 0 or len(fetchal(f"SELECT * FROM User WHERE id = '{user_id}'"))==0:
        raise HTTPException(status_code=401, detail="User not found")

    if len(fetchal(f"SELECT * FROM User WHERE password = '{password}'")) == 1:
        executes(f"DELETE FROM User WHERE id = {user_id}")
        return True
    else:
        return False

# Операция получения времени регистрации пользователя (Read)
@app.get("/user/{user_id}/get_reg_time", response_model=int)
def get_user_registration_time(user_id: int, password: str):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")

    user = users[user_id]
    if user.password == password:
        return user.registration_time  # Предположим, что вы храните время регистрации пользователя
    else:
        return False


# Операция сброса пароля пользователя (Update)
@app.put("/user/{user_id}/reset_password", response_model=bool)
def reset_user_password(user_id: int, time_create: datetime):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")

    user = users[user_id]
    # Проверяем, что время создания пользователя не превышает указанное время
    if (datetime.now() - user.registration_time).total_seconds() <= time_create.total_seconds():
        # Выполняем сброс пароля
        user.password = "new_password"
        return True
    else:
        return False


# Операции для ресурса бронирования аналогичными способами

# Модель данных бронирования пользователя
class UserBooking(BaseModel):
    user_id: int
    start: datetime
    duration: int
    comment: Optional[str] = None


# Хранилище данных для бронирования пользователя
user_bookings = []


# Операция добавления бронирования для пользователя
@app.post("/booking/{user}/add", response_model=int)
def create_user_booking(user: int, booking: Booking):
    if user < 0 or user >= len(users):
        raise HTTPException(status_code=404, detail="User not found")

    user_booking = UserBooking(user_id=user, **booking.dict())
    user_bookings.append(user_booking)
    return len(user_bookings) - 1


# Операция получения всех бронирований для пользователя
@app.get("/booking/{user}/getall", response_model=List[UserBooking])
def get_all_user_bookings(user: int):
    if user < 0 or user >= len(users):
        raise HTTPException(status_code=404, detail="User not found")

    user_bookings_list = [ub for ub in user_bookings if ub.user_id == user]
    return user_bookings_list


# Операция удаления бронирования для пользователя
@app.delete("/booking/{user}/{booking_id}/del", response_model=bool)
def delete_user_booking(user: int, booking_id: int, password: str):
    if user < 0 or user >= len(users):
        raise HTTPException(status_code=404, detail="User not found")

    if booking_id < 0 or booking_id >= len(user_bookings):
        raise HTTPException(status_code=404, detail="Booking not found")

    user_booking = user_bookings[booking_id]
    if user_booking.user_id == user:
        user_bookings.pop(booking_id)
        return True
    else:
        return False


# Операция обновления бронирования для пользователя
@app.put("/booking/{user}/{booking_id}/update", response_model=bool)
def update_user_booking(user: int, booking_id: int, booking: Booking, password: str):
    if user < 0 or user >= len(users):
        raise HTTPException(status_code=404, detail="User not found")

    if booking_id < 0 or booking_id >= len(user_bookings):
        raise HTTPException(status_code=404, detail="Booking not found")

    user_booking = user_bookings[booking_id]
    if user_booking.user_id == user:
        user_booking.start = booking.start
        user_booking.duration = booking.duration
        user_booking.comment = booking.comment
        return True
    else:
        return False

@app.on_event("shutdown")
async def shutdown():
    connection.close()
