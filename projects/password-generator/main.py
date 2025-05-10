from password_generator import PasswordGenerator

print("Welcome to PyPassword Generator v0.2, now Object Oriented")

pypassgen = PasswordGenerator()

try:
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    
except ValueError:
    print("Use integers, please!")
    
else:
    pypassgen.generate(nr_letters, pypassgen.letters)
    pypassgen.generate(nr_numbers, pypassgen.numbers)
    pypassgen.generate(nr_symbols, pypassgen.symbols)
    password = pypassgen.generate_password()
    print(f"Your password is: {password}")