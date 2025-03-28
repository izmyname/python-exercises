n = int(input("Insert number here: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i  # e.g if n = 3, then factorial = 1*1*2*3

print(factorial)
