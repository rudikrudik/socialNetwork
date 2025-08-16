import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Otus Highload"
    PROJECT_VERSION: str = "0.0.1"
    DB_HOST: str
    DB_PORT_READ: int
    DB_PORT_WRITE: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    SECRET_KEY: str
    ALGORITHM: str
    REDIS_CACHE_HOST: str
    REDIS_CACHE_LOGIN: str
    REDIS_CACHE_PORT: int
    REDIS_PASSWORD: str
    REDIS_DB: int
    REDIS_DIALOG_HOST: str
    REDIS_DIALOG_LOGIN: str
    REDIS_DIALOG_PORT: int
    REDIS_DIALOG_PASSWORD: str
    REDIS_DIALOG_DB: int
    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGODB_DB: str
    MONGODB_COLLECTIONS: str
    POST_NOTIFICATION_HOST: str
    POST_NOTIFICATION_PORT: int
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_QUEUE: str
    RABBITMQ_ROUTER_KEY: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )


settings = Settings()
