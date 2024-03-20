import os
from pymongo.mongo_client import MongoClient # pip install pymongo
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Create a new client and connect to the server
load_dotenv(".env")
uri = os.getenv("db_url") # Replace this with your DataBase Access
db_name = os.getenv("client_db")
collection_name = os.getenv("collection_db")
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

database = client[db_name]
collection = database[collection_name]


def insertPeriod(period, incomes, expenses, comment):
    return collection.insert_one({"period":period, "incomes":incomes, "expenses":expenses, "comment":comment})

# Get periods from database
def get_all_periods():
    items = collection.find()
    periods = [items["period"] for items in items]
    return periods

# Get all the info from an especific period
def get_period(period):
    res = collection.find_one({"period": period})
    return res

