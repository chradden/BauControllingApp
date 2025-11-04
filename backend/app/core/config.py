
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "BauControlling"
    APP_ENV: str = "dev"
    APP_SECRET: str = "change-me"
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/baucontrolling"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
