number = int(input("Insert a number here: ")) # self-explanatory
counter = 0 # we need this to count the numbers with each loop

while number != 0:
    # perform floor division to cut digits from a number
    number = number // 10
    counter += 1 # with each loop, floor division cuts one digit from a number and the value of counter increases. Thus, when number = 0 and the loop stops, the value of counter will be equal the number of digits.

print(counter)
