from pydantic import BaseModel, Field
from typing import Union
import datetime


class User(BaseModel):
    id: int = Field(examples=[1])
    first_name: str = Field(examples=["Имя"])
    last_name: str = Field(examples=["Фамилия"])
    birthday: Union[datetime.date, None] = Field(examples=["1998-01-01"])
    gender: Union[str, None] = Field(examples=["Пол"])
    hobby: Union[str, None] = Field(examples=["Хобби, интересы и т.п."])
    city: Union[str, None] = Field(examples=["Город"])


class CreateUser(BaseModel):
    first_name: str = Field(examples=["Имя"])
    last_name: str = Field(examples=["Фамилия"])
    birthday: datetime.date = Field(examples=["1998-01-01"])
    gender: str = Field(examples=["Пол"])
    hobby: str = Field(examples=["Хобби, интересы и т.п."])
    city: str = Field(examples=["Город"])
    login: str = Field(examples=["Имя входа"])
    password: str = Field(examples=["Пароль"])


class IdUser(BaseModel):
    id: int = Field(examples=[1])


class IdPost(BaseModel):
    id: int = Field(examples=[1])


class CreateUserPost(BaseModel):
    post_content: str = Field(examples=["Текст поста"])


class UpdateUserPost(BaseModel):
    id: int = Field(examples=[1])
    post_content: str = Field(examples=["Текст поста"])


class SearchUser(BaseModel):
    first_name: str = Field(examples=["Имя"])
    last_name: str = Field(examples=["Фамилия"])


class AuthUser(BaseModel):
    login: str = Field(examples=["login"])
    password: str = Field(examples=["password"])


class RegisterNewUser(BaseModel):
    first_name: str = Field(examples=["Имя"])
    last_name: str = Field(examples=["Фамилия"])
    login: str = Field(examples=["login"])
    password: str = Field(examples=["password"])


class UserPost(BaseModel):
    id_post: int
    id_user: int
    post_date: str
    post_content: str
    post_likes: str


class UserMessage(BaseModel):
    id_from: int
    to_id: int
    message: str
