import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import export_envs, load_secret
from settings import Settings


def test_main_script():
    export_envs("test")
    load_secret()

    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "test_app"
    assert settings.PROD_KEY1 == "test_value1"
    assert settings.PROD_KEY2 == "test_value2"
