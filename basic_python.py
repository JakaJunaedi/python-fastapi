import os
from dotenv import load_dotenv

# Memuat variabel dari file .env
load_dotenv()

# Mengambil variabel lingkungan
api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")

# Menampilkan variabel
print("API Key:", api_key)
print("Database URL:", database_url)
print("Secret Key:", secret_key)