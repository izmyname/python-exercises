ingredients = ["venison", "flour", "sugar", "cream",  "butter", "flour" , "eggs", "milk" ,"apple", "carrot", "syrup", "tomatoes", "milk", "rice", "salt", "chocolate",  "eggs", "pepper", "cream", "fish", "milk", "syrup",  "flour", "rice", "tomatoes", "sugar", "chocolate",  "salt", "fish", "carrot", "butter", "venison", "cream", "pepper"]

unique_ingredients = set(ingredients)

special_ingredients = { 
    frozenset(["cream", "chocolate", "syrup", "butter"]) : "Chef's special cake"
}


ingredients_count = {}

# We loop through unique ingredients set to fetch the key, then - we loop through ingredients list to count the amount of each ingredient 
# and assign them as values.
for i in unique_ingredients:
    ingredients_numbers = ingredients.count(i)
    ingredients_count[i] = ingredients_numbers

#print(ingredients_count)



# check for missing ingredients
def ingredients_check(ingredients_for_dish):
    missing_ingredients = ingredients_for_dish - unique_ingredients
    for ingredient in ingredients_for_dish:
        if ingredient in ingredients_count:
            if ingredients_count[ingredient] <= 0:
                missing_ingredients.add(ingredient)
    print(f"We are missing {missing_ingredients}")

# Ask our chef - how many and what ingredients to check for a dish
dish_to_prepare = set()

try:

    ingredients_amount = int(input("How many ingredients would you like to add? "))

except ValueError:
    print("Please, use numbers")

else:
    for i in range (1, ingredients_amount +1):
        ingredient_choice = input(" What ingredients would you like to add to your dish? ").lower()
        dish_to_prepare.add(ingredient_choice)
    ingredients_check(dish_to_prepare)


  # Sorry, no bonus here