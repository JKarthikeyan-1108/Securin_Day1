from fastapi import FastAPI
from database import collection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Recipe API using MongoDB"}

@app.get("/api/recipes")
def get_recipes(page: int = 1, limit: int = 10):

    skip = (page - 1) * limit

    recipes = (
        collection
        .find({}, {"_id": 0})
        .sort("rating", -1)
        .skip(skip)
        .limit(limit)
    )

    total = collection.count_documents({})

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": list(recipes)
    }