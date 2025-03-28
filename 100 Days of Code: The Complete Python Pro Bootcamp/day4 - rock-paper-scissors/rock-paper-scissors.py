# An exercise from Udemy 100 days of python bootcamp - day 4

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# We create list here to output ASCIIs instead of just raw text
game = [rock, paper, scissors]

# Prompt the player to make a choice and output an appropriate list item, in the player's choice is valid. 
player_choice = int(input("Type 0 for rock, 1 for paper and 2 for scissors: "))
if 0 <= player_choice <= 2:
    print(f"Your choice:\n {game[player_choice]}")


# For the computer choice - we'll use random module we've imported
#  It's the same as for the player, except we don't use an if statement for checking - whether the number is correct.
computer_choice = random.randint(0, 2)
print(f"Computer choice:\n {game[computer_choice]}")

# Use an if-elif statement to determine the winner
if player_choice == computer_choice:
    print("It's a draw!")
elif player_choice == 0 and computer_choice == 1:
    print("Computer won!")
elif player_choice == 0 and computer_choice == 2:
    print("You won!")
elif player_choice == 1 and computer_choice == 0:
    print("You won!")
elif player_choice == 1 and computer_choice == 2:
    print("Computer won!")
elif player_choice == 2 and computer_choice == 0:
    print("Computer won!")
elif player_choice == 2 and computer_choice == 1:
    print("You won!")
elif player_choice < 0 or player_choice > 2:
    print("Invalid number. Disqualified!")

