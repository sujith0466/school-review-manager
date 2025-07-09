import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "HOST": os.getenv("DB_HOST"),
    "USER": os.getenv("DB_USER"),
    "PASSWORD": os.getenv("DB_PASSWORD"),
    "DATABASE": os.getenv("DB_NAME")
}

SECRET_KEY = os.getenv("SECRET_KEY")
