from pydantic import BaseModel, Field
from typing import Union
import datetime


class IdUser(BaseModel):
    id: int = Field(examples=[1])


class UserFriends(BaseModel):
    id: int = Field(examples=[1])
    user_friends: list = Field(examples=[[1, 2, 3]])
