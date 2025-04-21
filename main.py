import argparse
import os
import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    load_dotenv(".env." + environment)


def load_secret() -> None:
    # Construct the file path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_file_path = os.path.join(current_dir, "secrets.yaml")

    # Load the YAML file
    with open(yaml_file_path, "r") as file:
        yaml_data = yaml.safe_load(file)

    # Access a specific variable and set it as an environment variable
    variable_key = "secret_password"
    if variable_key in yaml_data:
        os.environ["SECRET_KEY"] = yaml_data[variable_key]
        print(
            f"Environment variable '{variable_key}' set to: {os.environ['SECRET_KEY']}"
        )
    else:
        print(f"Key '{variable_key}' not found in YAML file.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    load_secret()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("SECRET_KEY: ", settings.SECRET_KEY)
