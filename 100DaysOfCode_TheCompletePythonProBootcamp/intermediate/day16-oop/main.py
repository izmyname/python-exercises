from turtle import Turtle, Screen
from prettytable import PrettyTable
from pip._vendor.rich import align

# Donatello = Turtle()
# Donatello.shape("turtle")
# Donatello.color("DarkRed")
# Donatello.forward(100)
# Donatello.right(30)
# Donatello.forward(30)
# Donatello.left(70)
# Donatello.forward(11)


# the_screen = Screen()
# #print(the_screen.canvheight)
# the_screen.exitonclick()


# # My solution
# table = PrettyTable(["Pokemon Name", "Type"])
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])

# print(table)

# # Correct solution
# table2 = PrettyTable()
# table2.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table2.add_column("Pokemon Type", ["Electric", "Water", "Fire"])

# print(table2)

# left-aligned
table3 = PrettyTable()
table3.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table3.add_column("Pokemon Type", ["Electric", "Water", "Fire"])
table3.align = "l"

print(table3)


