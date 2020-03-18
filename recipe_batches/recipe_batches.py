#!/usr/bin/python

import math


# cooking function
# input 1: recipe amt dictionary
# input 2: actual supply dictionary
# output: possible whole batches
def recipe_batches(recipe, ingredients):

    # plan:
    # for each actual supply number:
    # calculate the lowest multiple of that required
    # store that number in a list of batch numbers
    batch_numbers = []

    # iterate through ingredients dictionary
    # compare values between dictionaryies
    # note: since we don't know if the dictionaries
    # will always be in the same sequence or if
    # the 'available' list will include
    # zero quantitty items, the recipe will be consulted first
    # and that key will be used to look for a corresponding key
    # in the 'available' list

    # iterate through each key in the recipe list:
    exists = True

    whole_batches = []

    # then run:
    # https://www.geeksforgeeks.org/python-accessing-key-value-in-dictionary/
    # iterate through all keys and values of the recipe
    for key, value in recipe.items():

        # iterate through each key in the recipe list:
        if key in ingredients:
            exists = True
        else:
            exists = False

        # print(key)
        # print("recipe", value)
        recipy_value = value
        if exists == True:
            # when both exist
            # for each key, compare the value in ingredients
            # https://www.w3schools.com/python/python_dictionaries.asp
            ingredients_value = ingredients[key]
            # print("ingredients available", ingredients_value)
            # print("whole batches", ingredients_value//recipy_value)
            whole_batches.append(ingredients_value // recipy_value)
        else:
            # where no needed ingredients are to be had
            whole_batches.append(0)

    # print("all batches", whole_batches)
    # print("fewest whole batches", min(whole_batches))
    return min(whole_batches)


if __name__ == "__main__":
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {"milk": 100, "butter": 50, "flour": 5}
    ingredients = {"milk": 132, "butter": 48, "flour": 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}.".format(
            batches=recipe_batches(recipe, ingredients), ingredients=ingredients
        )
    )
