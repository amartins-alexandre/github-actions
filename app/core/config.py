import os

APP_PROFILE: str = os.getenv("ACTIVE_PROFILE", "dev")
SEM_VER: str = open(os.path.join(os.path.abspath(os.getcwd()), 'version.txt'), 'r').read().strip()
API_V1_STR: str = "/api/v1"

# Postgres
DB_USER: str = os.getenv("POSTGRES_USER", "postgres")
DB_PWD: str = os.getenv("POSTGRES_PWD", "123124")
DB_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT: str = os.getenv("POSTGRES_PORT", "5432")
DB_NAME: str = os.getenv("POSTGRES_DB", DB_USER)

DB_HOST_STRING = os.getenv("DB_HOST_STRING", f'postgresql+asyncpg://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
