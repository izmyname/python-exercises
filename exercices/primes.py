start = int(input("Enter the lower number: "))
end = int(input("Enter the higher number: "))

if start >= end:
    print("higher number must be bigger, than lower")

else:
    print("Prime numbers between", start, "and", end, "are: ", end=' ')

    # num is a number we're trying to divide to check - whether it's a prime number
    for num in range(start, end + 1):
        # if number <= 1, it can't be a prime number
        if num > 1:
            # i is a divisor. We're trying to divide num by i here.
            for i in range(2, num):
                # We excluded 1 and the number itself here, so if the number gets divided without a remainder - it's not a prime number
                if (num % i) == 0:
                    break

            else:
                print(num, end=' ')
