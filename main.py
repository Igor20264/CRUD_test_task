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
from BaseModels import User, Booking, Iser, Booking_Id  # Базовые модели
from fastapi.openapi.docs import get_swagger_ui_html

import bcrypt

import json
app = FastAPI()

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect('database.db', check_same_thread=False)

@app.get("/docs")
def read_docs():
    return get_swagger_ui_html(openapi_url="/openapi.json")

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

def chekhex(data,hash):
    if bcrypt.checkpw(bytes(data, 'utf-8'), bytes(hash, 'utf-8')):
        return True
    else: return False

def hex(data:str):
    data = bcrypt.hashpw(bytes(data, 'utf-8'), bcrypt.gensalt()).decode("utf-8")
    return data

# Операция создания пользователя (Create)
@app.post("/user/add", response_model=int)
def create_user(user: User)->int:
    if len(fetchal(f"SELECT * FROM User WHERE username = '{user.name}'"))==0:
        executes(f"INSERT INTO User (username, password, created, updated) VALUES ('{user.name}', '{hex(user.password)}', {int(time.time())}, {int(time.time())});")
        return fetchal(f"SELECT * "
                       f"FROM User "
                       f"WHERE username = {user.name} ;")[0][0]  # Возвращаем индекс созданного пользователя
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
@app.delete("/user/{user_id}/del", response_model=bool)
def delete_user(user_id:int,password: str):
    if user_id < 0 or len(fetchal(f"SELECT * FROM User WHERE id = '{user_id}'"))==0:
        raise HTTPException(status_code=401, detail="User not found")

    if chekhex(password,fetchal(f"SELECT password FROM User WHERE id = '{user_id}'")[0][0]):
        executes(f"DELETE FROM User WHERE id = {user_id}")
        executes(f"DELETE FROM Booking WHERE user_id = {user_id}")
        return True
    else:
        return False

# Операция получения времени регистрации пользователя (Read)
@app.get("/user/{user_id}/get_reg_time", response_model=int)
def get_user_registration_time(user_id: int, password: str):
    if user_id < 0 or len(fetchal(f"SELECT * FROM User WHERE id = '{user_id}'")) == 0:
        raise HTTPException(status_code=401, detail="User not found")

    if chekhex(password,fetchal(f"SELECT password FROM User WHERE id = '{user_id}'")[0][0]):
        time = fetchal(f"""
                SELECT created
                FROM User
                WHERE id = '{user_id}'
                """)
        return time[0][0]
    else:
        return -1

# Операция сброса пароля пользователя (Update)
@app.put("/user/{user_id}/reset_password", response_model=bool)
def reset_user_password(user_id: int, created: int,password:str):
    if user_id < 0 or len(fetchal(f"SELECT * FROM User WHERE id = '{user_id}'")) == 0:
        raise HTTPException(status_code=401, detail="User not found")

    ttime = int(fetchal(f"""
                    SELECT created
                    FROM User
                    WHERE id = '{user_id}'
                    """)[0][0])
    # Проверяем, что время создания пользователя не превышает указанное время
    if ttime == created:
        executes(f"""
        UPDATE User
        SET password = '{hex(password)}',
            updated = {int(time.time())}
        WHERE id = {user_id};
        """)
        return True
    else:
        return False

# Хранилище данных для бронирования пользователя
user_bookings = []
users = []

# Операция добавления бронирования для пользователя
@app.post("/booking/add", response_model=int)
def create_user_booking(booking: Booking):
    if booking.user_id < 0 or len(fetchal(f"SELECT * FROM User WHERE id = '{booking.user_id}'")) == 0:
        raise HTTPException(status_code=401, detail="User not found")
    if booking.comment:
        executes(f"INSERT INTO Booking (user_id, start_time, end_time, comment) VALUES ({booking.user_id}, {booking.start}, {booking.end}, '{booking.comment}');")
    else:
        executes(f"INSERT INTO Booking (user_id, start_time, end_time) VALUES ({booking.user_id}, {booking.start}, {booking.end});")

    return fetchal(f"SELECT id FROM Booking ORDER BY id DESC LIMIT 1;")[0][0]  # Возвращаем индекс созданного пользователя


# Операция получения всех бронирований для пользователя
@app.get("/booking/{user_id}/getall", response_model=List[list])
def get_all_user_bookings(user_id: int):
    data = fetchal(f"""
            SELECT *
            FROM Booking
            WHERE user_id == '{user_id}';
            """)
    return data

# Операция удаления бронирования для пользователя
@app.delete("/booking/{user_id}/{booking_id}/del", response_model=bool)
def delete_user_booking(user_id: int, booking_id: int, password: str):
    if user_id < 0 or len(fetchal(f"SELECT * FROM User WHERE id = '{user_id}'")) == 0:
        raise HTTPException(status_code=401, detail="User not found")

    if booking_id < 0 or len(fetchal(f"SELECT * FROM Booking WHERE id = '{booking_id}'")) == 0:
        raise HTTPException(status_code=401, detail="Booking not found")

    if chekhex(password, fetchal(f"SELECT password FROM User WHERE id = '{user_id}'")[0][0]):
        executes(f"DELETE FROM Booking WHERE id = {booking_id}")
        return True
    else:
        return False


# Операция обновления бронирования для пользователя
@app.put("/booking/{user_id}/{booking_id}/update", response_model=bool)
def update_user_booking(user_id: int, booking_id: int, booking: Booking, password: str):
    if user_id < 0 or len(fetchal(f"SELECT * FROM User WHERE id = '{user_id}'")) == 0:
        raise HTTPException(status_code=401, detail="User not found")

    if booking_id < 0 or len(fetchal(f"SELECT * FROM Booking WHERE id = '{booking_id}'")) == 0:
        raise HTTPException(status_code=401, detail="Booking not found")

    if chekhex(password, fetchal(f"SELECT password FROM User WHERE id = '{user_id}'")[0][0]):
        if booking.comment:
            executes(f"""
                    UPDATE Booking
                    SET start_time = {booking.start},
                        end_time = {booking.end},
                        comment = '{booking.comment}'
                    WHERE id = {booking_id} AND user_id = {user_id};
                    """)
        else:
            executes(f"""
                    UPDATE Booking
                    SET start_time = {booking.start},
                        end_time = {booking.end}
                    WHERE id = {booking_id} AND user_id = {user_id};
                    """)
        return True
    else:
        return False

@app.on_event("shutdown")
async def shutdown():
    connection.close()
