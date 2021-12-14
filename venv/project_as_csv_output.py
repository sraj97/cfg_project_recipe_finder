import requests
import csv


def api_call(user_ingredient):
    api_id = "55df2a1f"
    api_key = "88f4b7d5ab9dda029512524b9083f2a8"
    url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}".format(user_ingredient.lower(), api_id, api_key)
    response = requests.get(url)
    response = response.json()

    return response["hits"]


def save_recipes():
    with open('recipes.csv', 'r+') as recipe_csv_file:
        user_ingredient = input("What ingredient do you want a recipe for? ")
        recipes = api_call(user_ingredient)
        data = []
        field_names = ["Your Ingredient", "Recipe Name", "Yield", "Ingredients"]

        for i in recipes:
            data.append(
                {"Your Ingredient": user_ingredient.title(), "Recipe Name": i["recipe"]["label"],
                 "Yield": i["recipe"]["yield"],
                 "Ingredients": i["recipe"]["ingredientLines"]})

            spreadsheet = csv.DictWriter(recipe_csv_file, fieldnames=field_names)
            spreadsheet.writeheader()
            spreadsheet.writerows(data)


save_recipes()
