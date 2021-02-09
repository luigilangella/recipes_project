import os
import json


def write_data(data, filename="recipe.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def append_data():
    with open("recipe.json") as json_file:
        data = json.load(json_file)
        temp = data["Recipes"]
        temp.append(json_data)
    write_data(data)


a = 'Y'
start_file = {"Recipes": []}

while (a == 'Y'):
    category = str(input('Enter the category: ').capitalize())
    recipe_name = str(input('Enter recipe name: ').capitalize())
    if (os.path.exists('recipe.json')):
        with open('recipe.json') as f:
            data = json.load(f)
            while (recipe_name in data['Recipes'][0]['name']):
                recipe_name = str(
                    input("Name already exists\nenter a different name: ").capitalize())
    ingredients = str(input('Enter ingredients: ').capitalize())
    allergens = str(input('Enter the allergens: ').capitalize())
    json_data = {
        "category":  category,
        "name": recipe_name,
        "ingredients": ingredients,
        "allergens": allergens,
    }
    a = str(input("Do you want to continue? ").capitalize())
    if(a == 'Y'):
        if (not os.path.exists('recipe.json')):
            with open('recipe.json', 'w') as f:
                json.dump(start_file, f)
            append_data()
        else:
            append_data()
    elif (a == 'N'):
        append_data()
        break
    else:
        print("It must be a Y or N...")
        a = str(input("Do you want to continue? ").capitalize())
        append_data()
