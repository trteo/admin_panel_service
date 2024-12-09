from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)


class Settings(BaseSettings):
    DEV: bool = False

    POSTGRES_USER: str = ''
    POSTGRES_PASSWORD: str = ''
    POSTGRES_DATABASE: str = ''
    POSTGRES_HOST: str = ''
    POSTGRES_PORT: str = ''

    class Config:
        env_file = Path(BASE_DIR, 'admin_settings', 'env')


settings = Settings()

# settings = None

