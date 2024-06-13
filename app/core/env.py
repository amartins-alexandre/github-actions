import os

APP_PROFILE: str = os.getenv("APP_PROFILE", "dev")
API_V1_STR: str = "/api/v1"

# Postgres
DB_USER: str = os.getenv("POSTGRES_USER", "postgres")
DB_PWD: str = os.getenv("POSTGRES_PWD", "123124")
DB_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT: str = os.getenv("POSTGRES_PORT", "5432")
DB_NAME: str = os.getenv("POSTGRES_DB", DB_USER)
