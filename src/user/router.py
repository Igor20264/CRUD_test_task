from fastapi import APIRouter


router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.post("/user", response_model=dict)
def create_user(user: User):
    if len(fetchal(f"SELECT * FROM User WHERE username = '{user.name}'"))==0:
        executes(f"INSERT INTO User (username, password, created, updated) VALUES ('{user.name}', '{hex(user.password)}', {int(time.time())}, {int(time.time())});")
        return {"user_id":fetchal(f"SELECT * FROM User WHERE username = {user.name} ;")[0][0]}  # Возвращаем индекс созданного пользователя
    raise HTTPException(status_code=409, detail="User already exists")

# Операция проверки занятости имени пользователя (Read)
@router.get("/user/checkname", response_model=bool)
def check_username(username: str)->bool:
    if len(fetchal(f"""
    SELECT *
    FROM User
    WHERE username = '{username}'
    """))==0:
        return True
    raise HTTPException(status_code=409, detail="User already exists")

# Операция получения имени и id пользователя (Read)
@router.get("/user/id", response_model=dict)
def get_user_id_by_name(username: str):
    try:
        id = fetchal(f"""
        SELECT *
        FROM User
        WHERE username = '{username}'
        """)[0][0]
        return {"user_id":id}
    except Exception as error:
        raise HTTPException(status_code=401, detail="User not found")

# Операция получения всех пользователей (Read All)
@router.get("/user/all", response_model=List[tuple])
def get_all_users():
    return fetchal(f"""
        SELECT username,id
        FROM User;
        """)

# Операция удаления пользователя (Delete) Хз можно ли, так делать... Но это удаление...
@router.delete("/user", response_model=bool)
def delete_user(user_id:int,password: str):
    if user_id < 0 or len(fetchal(f"SELECT * FROM User WHERE id = '{user_id}'"))==0:
        raise HTTPException(status_code=401, detail="User not found")

    if chekhex(password,fetchal(f"SELECT password FROM User WHERE id = '{user_id}'")[0][0]):
        executes(f"DELETE FROM User WHERE id = {user_id}")
        executes(f"DELETE FROM Booking WHERE user_id = {user_id}")
        return True
    return False

# Операция получения времени регистрации пользователя (Read)
@router.get("/user/reg_time", response_model=dict)
def get_user_registration_time(user: UserId):
    if user.id < 0 or len(fetchal(f"SELECT * FROM User WHERE id = '{user.id}'")) == 0:
        raise HTTPException(status_code=401, detail="User not found")

    if chekhex(user.password,fetchal(f"SELECT password FROM User WHERE id = '{user.id}'")[0][0]):
        time = fetchal(f"""
                SELECT created
                FROM User
                WHERE id = '{user.id}'
                """)
        return {"time_crete":time[0][0]}
    return -1

# Операция сброса пароля пользователя (Update)
@router.put("/user/{user_id}/reset_password", response_model=bool)
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
    return False
