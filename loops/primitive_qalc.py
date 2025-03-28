# a simple calculator, that can be used with just two numbers
operator = input("Select an operator (+, -, *, /, ** or //): ")
num1 = float(input("Insert number 1: "))
num2 = float(input("Insert number 2: "))

if operator == "+":
    result = num1 + num2
    print(result)

elif operator == "-":
    result = num1 - num2
    print(result)

elif operator == "*":
    result = num1 * num2
    print(result)

elif operator == "/":
    result = num1 / num2
    print(result)

elif operator == "**":
    result = num1 ** num2
    print(result)

elif operator == "//":
    result = num1 // num2
    print(result)

else:
    print("Invalid operator.")


