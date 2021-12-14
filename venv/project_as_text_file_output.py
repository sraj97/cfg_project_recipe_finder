import requests
import csv


def api_call(user_ingredient, meal_type):
    api_id = "55df2a1f"
    api_key = "88f4b7d5ab9dda029512524b9083f2a8"
    url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}&mealType={}".format(user_ingredient.lower(), api_id,
                                                                                       api_key, meal_type.lower())

    response = requests.get(url)
    response = response.json()

    return response["hits"]


def save_recipes():
    with open('recipes_as_text.txt', 'r+') as recipe_text_file:
        recipe_text_file.read()

        meal_type = input("What meal are you looking for? (Breakfast, Lunch, Dinner) ")
        user_ingredient = input("What ingredient do you want a recipe for? ")
        recipes = api_call(user_ingredient, meal_type)

        recipe_text_file.write('Meal Type Searched: {}\n\nIngredient Searched: {}\n\n'.format(meal_type.title(),
                                                                                              user_ingredient.title()))

        for i in recipes:
            new_recipe = str(
                "Recipe Name: {}\nRecipe URL: {}\nYield: {}\nIngredients: \n"
                    .format(i["recipe"]["label"],i["recipe"]["uri"], i["recipe"]["yield"]))

            ingredients = i["recipe"]["ingredients"]
            list_of_ingredients = ""

            for ingredient in ingredients:
                each_ingredient = str(ingredient["text"] + '\n')

                list_of_ingredients += each_ingredient

            new_recipe = new_recipe + list_of_ingredients + '\n\n'

            recipe_text_file.write(new_recipe)
        recipe_text_file.write("**********\n\n\n")


save_recipes()
