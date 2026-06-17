from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

print("Loaded URI:", MONGO_URI)

client = MongoClient(MONGO_URI)

try:
    client.admin.command("ping")
    print("✅ Connected Successfully!")
except Exception as e:
    print("❌ Connection Error:")
    print(e)