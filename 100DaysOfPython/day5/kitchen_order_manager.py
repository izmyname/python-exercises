import random

meals = ["French Fries", "Burger", "Pizza", "Salad", "Chicken wings"]
prices = (5.49, 10.99, 15.20, 7.99, 9.99)
tax = (0.05, "USD")

print(f"Today's Menu:\n\n0 - {meals[0]} - ${prices[0]}\n1 - {meals[1]} - ${prices[1]}\n2 - {meals[2]} - ${prices[2]}\n3 - {meals[3]} - ${prices[3]}\n4 - {meals[4]} - ${prices[4]}\n")

chef_special = random.choice(meals)
print(f"{chef_special} is today's chef special!\n")


def kitchen():


    stop_ordering = False

    orders = []

    total_sum = 0

    while not stop_ordering:

        try:

            user_meal = int(input("What meal would you like to order? Choose between 0 and 4 "))
    
            chosen_meal = meals[user_meal]

        except ValueError:
            print("Oops, that's not a valid number. Please try again.")

        except IndexError:
            print("Sorry, this position is not in the menu")

        else:
            user_meal_quantity = int(input("How many would you like? "))
            
            meal_price = round((prices[user_meal] * user_meal_quantity), 2)

            order = f"{user_meal_quantity}x {chosen_meal} = ${meal_price}"

            total_sum += meal_price 

            total_sum -= round((total_sum* tax[0]), 2)

            orders.append(order)

            for item in orders:
                print(item)

            print(f"----------\nTotal = {total_sum}\n")

        finally:

            prompt_user = input("Anything else? y/n ")
            if prompt_user == "n":
                stop_ordering = True
                print("Thanks for visiting Python Kitchen!")

    
kitchen()
