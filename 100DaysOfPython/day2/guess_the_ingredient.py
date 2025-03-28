import random

print("Guess the secret ingredient")

ingredients = ["sugar", "eggs", "carrot", "cheese", "pepper", "chocolate", "rice"]

secret_ingredient = random.choice(ingredients)

right_guess = False

no_attempts = 0


while not right_guess:
    user_guess = input("What's the secret ingredient?\n type one of: sugar, eggs, carrot, cheese, pepper, chocolate, rice\n Your choice: ")
    no_attempts += 1

    if user_guess == secret_ingredient:
        print(f"Correct!\nIt took you {no_attempts} attempts to guess")
        right_guess = True
    else:
        print(f"Wrong! Try again.\nAttempt: {no_attempts}")
