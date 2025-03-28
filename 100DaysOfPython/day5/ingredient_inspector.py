ingredients = [ "pepper", "salt", "sugar", "tomato", "cucumber", "garlic"]

try:
    choice = int(input("What ingredient would you like to choose? Enter 0 - 5 "))
    print(f"You chose {ingredients[choice]}")

except ValueError:
    print("This is not a number")
except IndexError:
    print("Wrong number")
else:
    print("Thank you for your choice!")

finally:
    print("Have a nice day")

