import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    BASE_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Тут токены для api внешних и бота
    SENTIMENT_TOKEN: SecretStr
    SQLITE_DB_PATH: str = "sqlite+aiosqlite:///./clients.db"

    @property
    def DB_URL(self) -> str:
        return self.SQLITE_DB_PATH

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")


# Получаем настройки
settings = Settings()
database_url = settings.DB_URL
