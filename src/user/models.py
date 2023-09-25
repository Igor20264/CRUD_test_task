from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    password: str
class UserId(User): #Как юзер только с id
    id:int
    password:str

class DataUser(UserId):
    id: int
    name: str