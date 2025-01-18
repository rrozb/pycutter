from dotenv import load_dotenv
from pydantic import ConfigDict
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Application settings."""

    model_config = ConfigDict(
        env_file=".env",
        case_sensitive=True,
    )

    SOME_ENV_VAR: str = "some_env_var"


settings = Settings()
