# import os

# class Config:
#     SECRET_KEY = "dev-secret-key"
#     SQLALCHEMY_DATABASE_URI = os.getenv(
#         "DATABASE_URL", "sqlite:///tatrack.db"
#     )
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

import os

class Config:
    # Use an environment variable for the secret key in production
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    # Ensure compatibility with newer SQLAlchemy versions for PostgreSQL
    db_url = os.getenv("DATABASE_URL", "sqlite:///tatrack.db")
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)
    
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///tatrack.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False