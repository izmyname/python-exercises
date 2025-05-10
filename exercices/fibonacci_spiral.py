n = int(input("Insert a number: ")) # prompt user to insert a number

num1, num2 = 0, 1 # the first two numbers in a sequence

print("Fibonacci sequence for number", n, ": ") # fancy

# run loop n times
for i in range(n):

    result = num1 + num2 # get the next number in a sequence

    # update values
    num1 = num2
    num2 = result

    print(num1, end=' ') # print the next number in a sequence
