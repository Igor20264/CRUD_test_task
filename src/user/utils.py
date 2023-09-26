import uuid

import bcrypt
import edgedb
from fastapi import HTTPException

from queries import get_password_async_edgeql as get_password


async def password_cheker(executor: edgedb.AsyncIOExecutor,password:str, id: uuid.UUID):
    b_password = bytes(password, 'utf-8')
    try:
        hash = await get_password.get_password(executor, id=id)
        b_hash = bytes(hash.password, 'utf-8')
    except AttributeError:
        raise HTTPException(status_code=409, detail="Id not exists")
    return bcrypt.checkpw(b_password,b_hash)


async def create_hash(data: str) -> str:
    data = bcrypt.hashpw(bytes(data, 'utf-8'), bcrypt.gensalt()).decode("utf-8")
    return data
