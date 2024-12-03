import json

with open('homework_1_recipes.json') as recipes_file:
    recipes = json.load(recipes_file)

with open('homework_1_markets.json') as markets_file:
    markets = json.load(markets_file)

def find_stores(dish_name, recipes, markets):
    if dish_name not in recipes:
        return "Do Not Have A Recipe For This Dish"
    
    required_ingredients = set(recipes[dish_name]["ingredients"])
    stores_needed = []
    collected_ingredients = set()
    
    for store, products in markets.items():
        if required_ingredients - collected_ingredients:
            stores_needed.append(store)
            collected_ingredients.update(products)
    
    if not required_ingredients - collected_ingredients:
        return f"Stores Needed: {', '.join(stores_needed)}"
    else:
        return "The Dish Cannot Be Prepared In This City."

print("Available Dishes:", ", ".join(recipes.keys()))
user_dish = input("Which Dish Do You Want To Cook? ")

result = find_stores(user_dish, recipes, markets)
print(result)
