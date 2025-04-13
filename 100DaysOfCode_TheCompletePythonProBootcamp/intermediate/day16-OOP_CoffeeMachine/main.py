from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create components of our coffee machine, using existing classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


# Coffee Machine

coffee_machine_is_on = True  

selection = menu.get_items()

while coffee_machine_is_on:

    print("\n    ===Ultimate Python Object-Oriented Coffee Machine 3000 v0.2 (Powered by 󰣇  and )===  \n")
    
    user_choice = input(f"What would you like? {selection}  ").lower()
    
    user_drink = menu.find_drink(user_choice)
    
    if user_drink != None:
        if coffee_maker.is_resource_sufficient(user_drink) == True:
            if money_machine.make_payment(user_drink.cost) == True:
                coffee_maker.make_coffee(user_drink)
                

    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
        
    elif user_choice == "off":
        coffee_machine_is_on = False
        print("Termination signal received. Turning off")
    
