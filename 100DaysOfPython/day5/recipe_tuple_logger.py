recipe = ("flour", "sugar", "eggs", "butter")

print(f"\nTo bake a cake, you'll need:\n- a sack of {recipe[0]}\n- two cups of {recipe[1]}\n- six {recipe[2]}\n- {recipe[3]}")


try:
    recipe[0]="chocolate"
except TypeError:
    print("A friendly message - Don't alter the recipe")
finally:
    print("Have a nice cooking time! ")
