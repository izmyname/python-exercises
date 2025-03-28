class Chef:
    def __init__(self, name, specialisation):
        self.name = name
        self.specialisation = specialisation
        
    def cook(self, food):
        print(f"{self.specialisation} chef {self.name} is cooking {food}")
        
        
class SushiChef(Chef):
    
    def prepare(self, sushi):
        print(f"{self.name} is preparing {sushi}")
        
        
class PizzaChef(Chef):
    
    def make(self, pizza):
        print(f"{self.name} is making {pizza}")
        
class SaladChef(Chef):
    
    def slice(self, salad):
        print(f"{self.name} is preparing {salad}")
        

class Menu:
    
    def __init__(self):
        
        self.food = []
        
    def menu_add_food(self, food):
        self.food.append(food)
        
    def menu_list(self):
        for item in self.food:
            print(f" - {item}")
            

class Restaurant:
    
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.personnel = []
        
    
    def opening_time(self):
        print(f"{self.name} is open\nToday's menu")

        self.menu.menu_list()
        
    def hire_chefs(self, chef):
        self.personnel.append(chef)
        print(f"Welcome to {self.name}, chef {chef.name}")
        
    def personnel_list(self):
        print(f"{self.name}'s chefs")
        for chef in self.personnel:
            print(f"{chef.name} - {chef.specialisation}")
            
            
            
# Add separator for more readable output
def separator():
    print("\n===================\n")

# - Bonus: Use `@staticmethod` or `@classmethod` to define utility functions (like kitchen opening times)


# Our restaurant and chefs

place = Restaurant("Sapa food")
sushi_chef = SushiChef("Akira", "Japanese cuisine")
pizza_chef = PizzaChef("Rodrigo", "Italian cuisine")
salad_chef = SaladChef("Anna", "Greek cuisine")

# Hiring them
separator()
place.hire_chefs(sushi_chef)
place.hire_chefs(pizza_chef)
place.hire_chefs(salad_chef)
separator()
place.personnel_list()

# Open our restaurant and show the menu
separator()
place.menu.menu_add_food("Pizza margarita")
place.menu.menu_add_food("Pizza pepperoni")
place.menu.menu_add_food("Maki rolls")
place.menu.menu_add_food("Asaki rolls")
place.menu.menu_add_food("Greek salad")
place.menu.menu_add_food("Vegetarian salad")
place.opening_time()

