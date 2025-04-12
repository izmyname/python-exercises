MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee_machine_has_money = 0


def coffee_machine_resources():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = coffee_machine_has_money

    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"


def resources_are_sufficient(user_input):
    enough_resources = True

    for resource in MENU[user_input]['ingredients']:

        if resources[resource] < MENU[user_input]['ingredients'][resource]:
            print(f"Sorry, there isn't enough {resource}")
            enough_resources = False

    return enough_resources


def process_coins():
    """Yes, it's a chore, but that's what old coffee machines like."""
    total_inserted = 0

    insert_coins = True

    while insert_coins:

        try:
            select_coin = input("Please, insert the coins. quarter/dime/nickel/penny: ").lower()
            select_amount = int(input("How many coins would you like to insert? "))

        except ValueError:
            print("Incorrect data!")

        else:
            if select_coin == "quarter":
                total_inserted += (0.25 * select_amount)
            elif select_coin == "dime":
                total_inserted += (0.10 * select_amount)
            elif select_coin == "nickel":
                total_inserted += (0.05 * select_amount)
            elif select_coin == "penny":
                total_inserted += (0.01 * select_amount)
            else:
                print("Error. Please, try again")

        ask_for_more = input("Would you like to add more coins? y/n").lower()

        if ask_for_more == "n":
            insert_coins = False

    return total_inserted


def make_coffee(user_input):
    for resource in MENU[user_input]['ingredients']:
        resources[resource] = resources[resource] - MENU[user_input]['ingredients'][resource]

    print(f"Here's your {user_input}. Enjoy!")


coffee_machine_is_on = True

while coffee_machine_is_on:

    print("\n    ===Ultimate Python Coffee Machine 3000 v0.1 (Powered by 󰣇  and )===  \n")

    user_choice = input(f"What would you like? espresso/latte/cappuccino  ").lower()

    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":

        if resources_are_sufficient(user_choice):

            user_paid = process_coins()
            coffee_price = MENU[user_choice]['cost']

            if user_paid == coffee_price:
                coffee_machine_has_money += coffee_price
                make_coffee(user_choice)


            elif user_paid > coffee_price:
                coffee_machine_has_money += coffee_price
                change = user_paid - coffee_price
                make_coffee(user_choice)
                print(f"Here is ${change:.2f} in change")

            else:
                print("Sorry, that's not enough money. Money refunded")


    elif user_choice == "report":
        print(coffee_machine_resources())

    elif user_choice == "off":
        coffee_machine_is_on = False
        print("Termination signal received. Turning off")

    else:
        print("Incorrect choice.")
