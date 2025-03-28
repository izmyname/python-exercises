# Day 2 task from udemy's 100 Days of Code: The Complete Python Pro Bootcamp

# original task
print("This is a total bill calculator.")
bill = float(input("Your total bill $" ))
tip = int(input("Tip percentage you'd like to give "))
people = int(input("How many people to split the bill "))

# solution
tip = bill * (tip / 100)
bill_with_tip = bill + tip
bill_split = bill_with_tip / people
total = round(bill_split, 2)
print(f"Each of you should pay ${total}.")
