from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMINS: str
    REDIS_URL: str
    POSTGRES_URL: str
    ROOT_PASS: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
