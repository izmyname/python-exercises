input_num = int(input("Insert a number here: "))
power = int(input("Insert an exponent here: "))

for i in range(1, input_num + 1):
    rise = i**power

    print("Current number is: ", i, "the exponent is: ", power, "the result is: ", rise)
