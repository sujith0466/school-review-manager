from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    "HOST": os.getenv("DB_HOST"),
    "USER": os.getenv("DB_USER"),
    "PASSWORD": os.getenv("DB_PASSWORD"),
    "DATABASE": os.getenv("DB_NAME")
}
