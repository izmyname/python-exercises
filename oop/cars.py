class Car:
    def __init__(self, color, model, fuel):
        self.color = color
        self.model = model
        self.fuel = fuel
        
    def drive(self):
        print(f"{self.color} {self.model} moves forward, using {self.fuel}")
        
        
my_car = Car("red", "toyota", "gasoline")
my_car.color = "black"
my_car.drive()
print(my_car.fuel)


class EMobile(Car):
    
    def drive(self):
        print(f"{self.color} {self.model} won't go anywhere, because it has no {self.fuel}")

new_car = EMobile("blue", "tesla", "electricity")
new_car.color = "yellow"
new_car.drive()