from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = 'Diabetes Api'
    USERS_OPEN_REGISTRATION = False

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    ALGORITHM: str = "HS256"

    SECRET_KEY: str = None
    DATABASE_URL: str = None

    MAIL_USERNAME: str = None
    MAIL_PASSWORD: str = None
    MAIL_PORT = 587
    MAIL_SERVER: str = "smtp.gmail.com"

    FIRST_SUPERUSER: str = None
    FIRST_SUPERUSER_PASSWORD: str = None

    WATSON_API_KEY: str = None
    WATSON_VERSION: str = None
    WATSON_ASSISTANT_ID: str = None

    TEXT_SPEECH_API_KEY: str = None
    TEXT_SPEECH_URL: str = None

    TEXT_TO_SPEECH_ENGINE: str = "aws"
    class Config:
        env_file = '.env'


settings = Settings()
