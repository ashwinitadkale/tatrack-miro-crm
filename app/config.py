import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "tatrack-dev-secret-change-in-prod")

    _db_url = os.getenv("DATABASE_URL", "sqlite:///tatrack.db")

    # Render provides postgres:// but SQLAlchemy needs postgresql://
    if _db_url.startswith("postgres://"):
        _db_url = _db_url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = _db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Prevents dropped connections on Render's PostgreSQL
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 300,
    }
