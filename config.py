import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Basic configuration for the Flask app."""

    # Change this to a strong, random value in production
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")

    # SQLite database in the instance/ folder
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "instance", "app.db"),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

