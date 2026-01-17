import os

class Config:
    SECRET_KEY = "dev-secret-key"
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite:///tatrack.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
