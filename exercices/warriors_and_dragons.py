class Warrior:  # Blueprint for all warrior characters
    def __init__(self, name, health=100):
        self.name = name     # Every warrior has a name
        self.health = health # ...and health points
    
    def attack(self):
        print(f"{self.name} swings a sword! ⚔️")
        
        
        
class Dragon(Warrior):
    def attack(self):
        print(f"{self.name} breathes fire! 🔥")
        
        
        
human = Warrior("Dovahkin")
human.attack()
dragon = Dragon("Alduin")
dragon.attack()