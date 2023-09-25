import bcrypt
import edgedb
from queries import get_password_async_edgeql as get_password


async def password_cheker(executor: edgedb.AsyncIOExecutor, username: str):
    return bcrypt.checkpw(bytes(data, 'utf-8'),
                   bytes(get_password.get_password(executor, username=username)["password"], 'utf-8'))


async def create_hash(data: str) -> str:
    data = bcrypt.hashpw(bytes(data, 'utf-8'), bcrypt.gensalt()).decode("utf-8")
    return data
