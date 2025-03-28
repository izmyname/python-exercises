class Car:
    def __init__(self, color, model, fuel):
        self.color = color
        self.model = model
        self.fuel = fuel
        
    def drive(self):
        print(f"{self.color} {self.model} moves forward, using {self.fuel}")
        
        
my_car = Car("red", "toyota", "gas")
my_car.drive()


class EMobile(Car):
    
    def drive(self):
        print(f"{self.color} {self.model} won't go anywhere, because it has no {self.fuel}")
              
new_car = EMobile("blue", "tesla", "electricity")
new_car.drive()