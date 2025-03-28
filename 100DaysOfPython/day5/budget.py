menu = [ "pizza", 'burger', "french fries"]

prices = ( 15.99, 12.45, 5,00 )

try:
    ask_pizza = int(input(f"How many {menu[0]}s do you want? "))
    ask_burger = int(input(f"How many {menu[1]}s do you want? "))
    ask_fries = int(input(f"How many {menu[2]} do you want? "))

except ValueError:
    print("Please, use valid numbers")

else:
    total_pizza = ask_pizza * prices[0]
    total_burger = ask_burger * prices[1]
    total_fries = ask_fries * prices[2]

    total = total_pizza + total_burger + total_fries
    print(f"The total price is {total}.")

finally:
    print("Have a nice day!")
