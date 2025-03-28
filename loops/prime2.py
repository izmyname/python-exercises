start = int(input("start num: "))
end = int(input("end num: "))

if start>end:
    print("Nope: ")

else:
    print("Numbers between", start, "and", end, "are :")
    # num is what we're gonna divide here
    for num in range(start, end + 1):
        # 1, 0 and negative numbers can't be prime numbers
        if num > 1:
            # i is a divisor here
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
