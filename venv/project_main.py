import requests
import csv

api_id = "55df2a1f"
api_key = "88f4b7d5ab9dda029512524b9083f2a8"


def api_call(api_id, api_key):
    user_ingredient = input("What ingredient do you want a recipe for? ")
    url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}".format(user_ingredient.islower(), api_id, api_key)
    response = requests.get(url)
    response = response.json()

    recipes = response["hits"]
    data = []
    field_names = ["Recipe Name", "Ingredients"]

    for i in recipes:
        data.append(
            {"Recipe Name": i["recipe"]["label"], "Ingredients": i["recipe"]["ingredientLines"]})

    with open('recipes.csv', 'w+') as recipe_csv_file:
        spreadsheet = csv.DictWriter(recipe_csv_file, fieldnames=field_names)
        spreadsheet.writeheader()
        spreadsheet.writerows(data)


api_call(api_id, api_key)
