from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    PROJECT_NAME: str = "FastAPI Backend"
    API_V1_STR: str = "/api/v1"
    
    # Secret Key
    SECRET_KEY: str = "secret-key-placeholder"
    
    # DB URL
    DATABASE_URL: str = "sqlite:///./sql_app.db"

settings = Settings()
