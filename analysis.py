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

print(df)

print("\nTotal Sales:")
print(df["sales"].sum())

print("\nAverage Sales:")
print(df["sales"].mean())

print("\nHighest Sales Product:")
print(df.loc[df["sales"].idxmax()])

print("\nCategory Wise Sales:")
print(df.groupby("category")["sales"].sum())