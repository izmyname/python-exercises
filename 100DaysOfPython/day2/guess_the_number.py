import random

print("Guess the number between 1 and 12.")

secret_number = random.randint(1, 12)

right_guess = False

no_attempts = 0


while not right_guess:
    user_guess = int(input("What's your number? "))
    no_attempts += 1

    if user_guess == secret_number:
        print(f"Correct!\nIt took you {no_attempts} attempts to guess")
        right_guess = True
    elif user_guess < secret_number:
        print(f"Too small!\nAttempt: {no_attempts}")
    else:
        print(f"Too large!\nAttempt: {no_attempts}")

