from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="FLOWDESK_", extra="ignore")
    app_name: str = "flowdesk-api"
    env: str = "dev"
    paper_only: bool = True


settings = Settings()
