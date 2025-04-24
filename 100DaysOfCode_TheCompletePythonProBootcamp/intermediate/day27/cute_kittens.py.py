print("There are no kittens in this file =(\n")

# def all_sum(*args):
#     print(sum(args))

# all_sum(3, 5, 6)

def calculate(n, **kwargs):
    print(kwargs)
    print(n)
    n += kwargs["add"]
    n*= kwargs["multiply"]
    print(n)
    
    
calculate(2, foo="bar", add=10, multiply = -2, keke=44, kitten=False)


# class Kitten:
    
#     def __init__ (self, **kwargs):
#         self.name = kwargs["name"]
#         self.fur = kwargs["fur"]
#         self.sound = kwargs["sound"]
        
#     def sound2(self):
#         print(f"My kitty says {self.sound}")
    
# kitty = Kitten(name="Pebbles", fur="red", sound="meow")
# kitty.sound2()