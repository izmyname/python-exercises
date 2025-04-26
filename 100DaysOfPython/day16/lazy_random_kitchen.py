import random

def serve_dishes(dishes):
    for dish in dishes:
        yield dish

orders = ["pasta", "burger", "noodles", "pizza", "rice"]
random.shuffle(orders)
customers = ["John", "Dave", "Eivana", "Lynn", "Elyssa"]
random.shuffle(customers)

diner = serve_dishes(orders)

customers_orders ={
    
}

for c in customers:
    
    serve = next(diner)  
    print(f"Now serving {serve} for {c}")
    customers_orders[c]=serve
    
    
print(customers_orders)