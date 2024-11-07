from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    host: str
    port: int
    user: str
    password: str
    database: str
    echo: bool

    class Config:
        env_file = ".env"
        env_prefix = "DB_"
        env_file_encoding = "utf-8"


class TelegramSettings(BaseSettings):
    bot_token: str

    class Config:
        env_file = ".env"
        env_prefix = "TLG_"
        env_file_encoding = "utf-8"


class Settings(BaseSettings):
    load_dotenv()
    database: DatabaseSettings = DatabaseSettings()
    telegram: TelegramSettings = TelegramSettings()


settings = Settings()
