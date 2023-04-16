from pyfzf.pyfzf import FzfPrompt
from food_keys import get_food_keys
from get_correct_amount import get_correct_amount
import numpy as np

import json

with open('food_inventory.json', 'r') as data:
    food_inventory = json.load(data)


def create_recipe():
    fzf = FzfPrompt()
    recipe = {}
    ingredient = {}
    q1 = input("Add recipe name. ")
    q2 = input("Add recipe type. ")
    q3 = input("Add cook time. ")
    q4 = input("Add portion. ")
    recipe["name"] = q1
    recipe["type"] = q2
    recipe["cook time"] = q3
    recipe["portion"] = int(q4)

    while True:
        choice = fzf.prompt(get_food_keys())
        amount = fzf.prompt([n / 10 for n in range(0, 21)] + [*range(3, 21)])
        if food_inventory[choice[0]]["unit"] == "ks":
            amount[0] = float(amount[0]) / food_inventory[choice[0]]["amount"]
        # get_correct_amount(food_inventory, choice, amount)
        ingredient[choice[0]] = float(amount[0])
        recipe["ingredients"] = ingredient
        q5 = input("Do you want to add another ingredient? y/n ")
        if q5 == "n":
            break
    return recipe
