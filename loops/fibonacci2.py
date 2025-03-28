n = int(input("Enter a number of sequences: "))

# set initial values for the first two elements of a sequence
num1 = 0
num2 = 1

for i in range(n):
    num3 = num1 + num2 # the next number in a sequence

    #update vars for each new loop
    num1 = num2
    num2 = num3

    print(num1, end=' ')
