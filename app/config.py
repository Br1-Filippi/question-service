import os

class Settings:
    ENV = os.getenv("ENV", "development")
    DEBUG = ENV != "production"
    UPLOAD_DIR = "uploads"

settings = Settings()
