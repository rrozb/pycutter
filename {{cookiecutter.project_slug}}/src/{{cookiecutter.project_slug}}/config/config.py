"""Configuration module for {{ cookiecutter.project_name }}."""

from functools import lru_cache
from pathlib import Path
from typing import ClassVar

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    """Application settings."""

    SOME_ENV_VAR: str = "some_env_var"

    class Config:
        """Pydantic config class."""

        env_file: ClassVar[str | Path] = ".env"
        case_sensitive: ClassVar[bool] = True


settings = Settings()
