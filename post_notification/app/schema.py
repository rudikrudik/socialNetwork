from pydantic import BaseModel, Field


class UserFriends(BaseModel):
    id: int = Field(examples=[1])
    friends: list = Field(examples=[2, 3, 4])