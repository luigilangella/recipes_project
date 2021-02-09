import os
import json


def loader(json_data):
    start_file = {"Recipes": []}

    def write_data(data, filename="recipe.json"):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def append_data():
        with open("recipe.json") as json_file:
            data = json.load(json_file)
            temp = data["Recipes"]
            temp.append(json_data)
        write_data(data)

    if (not os.path.exists('recipe.json')):
        with open('recipe.json', 'w') as f:
            json.dump(start_file, f)
        append_data()
    else:
        append_data()
