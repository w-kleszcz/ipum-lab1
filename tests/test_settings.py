import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from settings import Settings  # Import Settings after modifying sys.path


def test_environment_is_valid():
    # Test that the ENVIRONMENT field is set correctly
    settings = Settings(
        ENVIRONMENT="dev",
        APP_NAME="TestApp",
        SECRET_KEY="supersecret",
        PROD_KEY1="prod_key1",
        PROD_KEY2="prod_key2",
    )
    assert settings.ENVIRONMENT == "dev"


def test_app_name_is_set():
    # Test that the APP_NAME field is set correctly
    settings = Settings(
        ENVIRONMENT="dev",
        APP_NAME="TestApp",
        SECRET_KEY="supersecret",
        PROD_KEY1="prod_key1",
        PROD_KEY2="prod_key2",
    )
    assert settings.APP_NAME == "TestApp"


def test_secret_key_is_set():
    # Test that the SECRET_KEY field is set correctly
    settings = Settings(
        ENVIRONMENT="dev",
        APP_NAME="TestApp",
        SECRET_KEY="supersecret",
        PROD_KEY1="prod_key1",
        PROD_KEY2="prod_key2",
    )
    assert settings.SECRET_KEY == "supersecret"


def test_prod_keys_are_set():
    # Test that PROD_KEY1 and PROD_KEY2 fields are set correctly
    settings = Settings(
        ENVIRONMENT="dev",
        APP_NAME="TestApp",
        SECRET_KEY="supersecret",
        PROD_KEY1="prod_key1",
        PROD_KEY2="prod_key2",
    )
    assert settings.PROD_KEY1 == "prod_key1"
    assert settings.PROD_KEY2 == "prod_key2"
