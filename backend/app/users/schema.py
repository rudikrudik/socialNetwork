from pydantic import BaseModel, Field
import datetime


class User(BaseModel):
    id: int = Field(examples=[1])
    first_name: str = Field(examples=["Имя"])
    last_name: str = Field(examples=["Фамилия"])
    birthday: datetime.date  = Field(examples=["1998-01-01"])
    gender: str = Field(examples=["Пол"])
    hobby: str = Field(examples=["Хобби, интересы и т.п."])
    city: str = Field(examples=["Город"])


class CreateUser(BaseModel):
    first_name: str = Field(examples=["Имя"])
    last_name: str = Field(examples=["Фамилия"])
    birthday: datetime.date = Field(examples=["1998-01-01"])
    gender: str = Field(examples=["Пол"])
    hobby: str = Field(examples=["Хобби, интересы и т.п."])
    city: str = Field(examples=["Город"])
    login: str = Field(examples=["Имя входа"])
    password: str = Field(examples=["Пароль"])


class AuthUser(BaseModel):
    login: str = Field(examples=["Имя входа"])
    password: str = Field(examples=["Пароль"])
