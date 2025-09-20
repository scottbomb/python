#!/usr/bin/env python
def get_omelet_ingredients(omelet_name):
    ingredients = {"eggs": 2, "milk": 1, "cheese": 1}
    if omelet_name == "mexican":
        ingredients ["chorizo"] = 2
        ingredients ["onion"] = 1
        ingredients ["bell pepper"] = 1
    elif omelet_name == "veggie":
        ingredients ["onion"] = 1
        ingredients ["bell pepper"] = 1
        ingredients ["mushrooms"] = 1
    elif omelet_name == "cheese":
        ingredients ["cheese"] = 2
    else:
        print("Sorry, that's not on the menu.")
        return None
    return ingredients

def make_food(ingredients_needed, food_name):
    for ingredient in ingredients_needed.keys():
        print ("Adding %d of %s to make a %s" %
               (ingredients_needed[ingredient], ingredient, food_name))
    print("Made %s" % food_name)
    return food_name

print("Let's make an omelet!")
wanted = input("What kind shall we make? ")
omelet = get_omelet_ingredients(wanted)
food = make_food(omelet,wanted)
print("We made a %s. All done!" % food )
