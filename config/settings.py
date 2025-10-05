import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///invoice_database.db")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
