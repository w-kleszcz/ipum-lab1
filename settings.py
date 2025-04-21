# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator, ValidationError


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    SECRET_KEY: str
    PROD_KEY1: str
    PROD_KEY2: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, v):
        # prepare validator that will check whether the value of ENVIRONMENT is in (dev, test, prod)
        if v not in ("dev", "test", "prod"):
            raise ValidationError("ENVIRONMENT must be one of: dev, test, prod")
        return v
