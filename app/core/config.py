from pydantic import BaseSettings


class Settings(BaseSettings):
OPENAI_API_KEY: str | None = None
MODEL_NAME: str = "gpt-4o-mini" # replace as needed
MAX_TOKENS: int = 1500
LOG_LEVEL: str = "info"


class Config:
env_file = ".env"


settings = Settings()