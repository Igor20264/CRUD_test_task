from typing import List
from fastapi import APIRouter, HTTPException
from src.user.models import UserId, User, UserReset,NewPassword,NewName
import edgedb

from src.queries import create_user_async_edgeql as create_user
from src.queries import chek_user_async_edgeql as chek_user
from src.queries import delete_user_async_edgeql as delete_user
from src.queries import get_id_async_edgeql as get_id_async
from src.queries import get_reg_time_async_edgeql as get_reg_time
from src.queries import get_users_async_edgeql as get_users
from src.queries import reset_password_async_edgeql as reset_password
from src.queries import reset_username_async_edgeql as reset_username
from src.user.utils import create_hash,password_cheker
router = APIRouter(
    prefix="/user",
    tags=["User"]
)
client = edgedb.create_async_client()

@router.post("/", response_model=create_user.CreateUserResult)
async def new_user(user: User):
    try:
        s = await create_user.create_user(client,username=user.name,password=create_hash(user.password))
        return s
    except edgedb.errors.ConstraintViolationError:
        raise HTTPException(status_code=409, detail="User already exists")


# Операция проверки занятости имени пользователя (Read)
@router.get("/checkname", response_model=bool)
async def check_username(username: str) -> bool:
    return await chek_user.chek_user(client,username=username)
    # raise HTTPException(status_code=409, detail="User already exists")


# Операция получения всех пользователей (Read All)
@router.get("/all", response_model=list[get_users.GetUsersResult])
async def get_all_users():
    return await get_users.get_users(client)


@router.delete("/", response_model=delete_user.DeleteUserResult)
async def delete_user(user: UserId):
    if await password_cheker(client, user.name):
        return await delete_user.delete_user(client,id=UserId,name=UserId.name)
    raise HTTPException(status_code=403, detail="Password is not corrected")

# Операция получения времени регистрации пользователя (Read)
@router.get("/reg_time", response_model=get_reg_time.GetRegTimeResult)
async def get_user_registration_time(user: UserId):
    if await password_cheker(client, user.name):
        return await get_reg_time.get_reg_time(client,id=user.id, username=user.name)
    raise HTTPException(status_code=403, detail="Password is not corrected")


# Операция сброса пароля пользователя (Update)
@router.put("/password", response_model=reset_password.ResetPasswordResult)
async def reset_user_password(user: NewPassword):
    return await reset_password.reset_password(client,id=user.id,username=user.name,created=user.created,password=user.newpassword)


# Операция сброса пароля пользователя (Update)
@router.put("/name", response_model=reset_username.ResetUsernameResult)
async def reset_user_password(user: NewName):
    if await password_cheker(client, user.name):
        return await reset_username.reset_username(client,id=user.id,username=user.newname)
    raise HTTPException(status_code=403, detail="Password is not corrected")