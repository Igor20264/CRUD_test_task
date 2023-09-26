import datetime

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
class User(BaseModel):
    name: str
    password: str

class UserId(User):
    id: str

class UserReset(UserId):
    created: datetime.datetime

class NewPassword(UserReset):
    newpassword: str

class NewName(UserReset):
    newname: str
class DataUser(BaseModel):
    id: str
    name: str