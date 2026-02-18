import json
from database import collection

with open("recipes.json", "r", encoding="utf-8") as file:
    data = json.load(file)

recipes = []

# If JSON is dictionary containing recipes inside
if isinstance(data, dict):
    data = list(data.values())

# Now loop safely
for item in data:

    if isinstance(item, dict):

        recipe = {
            "cuisine": item.get("cuisine"),
            "title": item.get("title"),
            "rating": item.get("rating"),
            "prep_time": item.get("prep_time"),
            "cook_time": item.get("cook_time"),
            "total_time": item.get("total_time"),
            "description": item.get("description"),
            "nutrients": item.get("nutrients"),
            "serves": item.get("serves")
        }

        recipes.append(recipe)

if recipes:
    collection.insert_many(recipes)
    print("Data inserted successfully")
else:
    print("No valid recipes found")