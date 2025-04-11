from art import logo

# define our functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# store functions in a dictionary
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

# calculator

def calculator():
    from art import logo
    print(logo)

    keep_going = True # A variable to keep a while loop up

    num1 = float(input("Insert the first number: ")) # We keep it outside the loop, in case if user wants to work with prev. result

    while keep_going: # starting our loop

        for key in operations:
            print(key)

        operator=input("Insert the operator: ")

        num2 = float(input("Insert the second number: "))

        result = operations[operator](num1, num2)

        print(f"{num1} {operator} {num2} = {result}")
        ask_user = input(f" Enter 'y' to continue with {result}, 'n to start from scrath, anything else to exit")
        if ask_user == "y":
            num1 = result
        elif ask_user == "n":
            keep_going = False
            calculator()
        else:
            keep_going = False
            print("Bye!")

calculator()