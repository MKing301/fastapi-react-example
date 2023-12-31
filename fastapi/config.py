from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    pg_user: str
    pg_pass: str
    pg_host: str
    pg_port: str
    pg_dbname: str

    class Config:
        env_file=".env"


settings = Settings()
