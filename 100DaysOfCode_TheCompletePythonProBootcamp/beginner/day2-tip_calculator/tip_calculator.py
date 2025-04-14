print("Welcome to the tip calculator!")

try:
    bill = float(input("What was the total bill? $"))
    tip = int(input("What percentage tip would you like to give? 10 12 15 "))
    people = int(input("How many people to split the bill? "))

except ValueError:
    print("use float for bill and integers for tip and people")
    
else:
    
    tip_percent = tip / 100
    tip_result = bill * tip_percent
    total_bill = bill + tip_result
    amount_per_person = total_bill / people
    total = round(amount_per_person, 2)

    print(f"Each of you has to play ${total:.2f}")
