from fastapi import APIRouter, HTTPException
from src.user.models import UserId, User, NewPassword,NewName
import edgedb
import uuid
from queries import chek_user_async_edgeql as chek_user, reset_password_async_edgeql as reset_password, \
    get_users_async_edgeql as get_users, delete_user_async_edgeql as delete_user, \
    get_reg_time_async_edgeql as get_reg_time, create_user_async_edgeql as create_user, \
    reset_username_async_edgeql as reset_username
from src.user.utils import create_hash,password_cheker
router = APIRouter(
    prefix="/user",
    tags=["User"]
)
client = edgedb.create_async_client()

@router.post("/", response_model=create_user.CreateUserResult)
async def new_user(user: User):
    try:
        s = await create_user.create_user(client,username=user.name,password=await create_hash(user.password))
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


@router.delete("/", response_model=bool)
async def user_delete(user: UserId):
    if await password_cheker(client,user.password, uuid.UUID(user.id)):
        data = await delete_user.delete_user(client,id=uuid.UUID(user.id),name=user.name)
        return bool(data)
    raise HTTPException(status_code=403, detail="Password is not corrected")

# Операция получения времени регистрации пользователя (Read)
@router.get("/reg_time", response_model=get_reg_time.GetRegTimeResult)
async def get_user_registration_time(user: UserId):
    if await password_cheker(client,user.password, uuid.UUID(user.id)):
        return await get_reg_time.get_reg_time(client,id=uuid.UUID(user.id), username=user.name)
    raise HTTPException(status_code=403, detail="Password is not corrected")


# Операция сброса пароля пользователя (Update)
@router.put("/password", response_model=reset_password.ResetPasswordResult)
async def reset_user_password(user: NewPassword):
    data = await reset_password.reset_password(client,id=uuid.UUID(user.id),username=user.name,created=user.created,password=await create_hash(user.newpassword))
    return data

# Операция сброса пароля пользователя (Update)
@router.put("/name", response_model=bool)
async def reset_user_name(user: NewName):
    print(user)
    if await password_cheker(client, user.password, uuid.UUID(user.id)):
        data = await reset_username.reset_username(client, id=uuid.UUID(user.id), username=user.name)
        return bool(data)
    raise HTTPException(status_code=403, detail="Password is not corrected")