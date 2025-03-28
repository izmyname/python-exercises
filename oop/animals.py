class Animal:
    
    def __init__(self, name, age):
        
        self.name = name
        self.age = age 
        
    def sound(self, voice):
        print(f"{self.name} is {self.age} years old. {self.name} says {voice}")
        
spider = Animal("Lucas", "2")
spider.sound("nothing")


class Dog(Animal):
    
    def sound(self, voice):
        print(f"{self.name} is {self.age} old. {self.name} is a good boy, he says {voice}")
        
    def bark(self, voice):
        print(f"{voice}-{voice}-{voice}")
        

dog = Dog("Dogmeat", 5)
dog.sound("woof")
dog.bark("bark")