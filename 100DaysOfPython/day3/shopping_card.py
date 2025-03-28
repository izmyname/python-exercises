item = input("What item would you like to buy?: ")  
price = float(input("What is the price?: "))
amount = int(input("How many would you like?: "))

total = price * amount

# Discount
if total >= 5000:
    total -= (total*0.1)

# Delivery Fee
if total < 3000:
    delivery_fee = 300
else:
    delivery_fee = 0

final_amount = total + delivery_fee


print(f"You bought {amount} {item} for ₦{price} each.\nTotal: ₦{total}\nDelivery Fee: ₦{delivery_fee}\nFinal Amount: ₦{final_amount}")

