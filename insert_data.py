from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["SalesDB"]

sales = db["Sales"]

sales.delete_many({})

sales.insert_many([
    {"product":"Laptop","category":"Electronics","sales":50000},
    {"product":"Mobile","category":"Electronics","sales":30000},
    {"product":"Shirt","category":"Fashion","sales":10000},
    {"product":"Jeans","category":"Fashion","sales":15000},
    {"product":"Book","category":"Education","sales":5000},
    {"product":"Notebook","category":"Education","sales":3000}
])

print("Sales Data Inserted Successfully!")