from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["recipes_db"]
collection = db["recipes"]