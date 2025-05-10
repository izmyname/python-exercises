# prompt user for a number
multiplier = int(input("Insert a multiplier: "))

# using a for loop to output the results of multiplication from 1 to 10
for num in range(1, 11):
    # fancy multiplication table
    print(multiplier, "X", num, "=", multiplier*num)
