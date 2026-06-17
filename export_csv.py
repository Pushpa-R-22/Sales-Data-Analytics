import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["SalesDB"]

sales = db["Sales"]

data = list(sales.find())

df = pd.DataFrame(data)

df.to_csv("sales_report.csv", index=False)

print("CSV Report Created Successfully!")