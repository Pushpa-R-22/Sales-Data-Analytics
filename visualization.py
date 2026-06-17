import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["SalesDB"]

sales = db["Sales"]

data = list(sales.find())

df = pd.DataFrame(data)

category_sales = df.groupby("category")["sales"].sum()

plt.bar(category_sales.index, category_sales.values)

plt.title("Category Wise Sales")

plt.xlabel("Category")

plt.ylabel("Sales Amount")

plt.show()