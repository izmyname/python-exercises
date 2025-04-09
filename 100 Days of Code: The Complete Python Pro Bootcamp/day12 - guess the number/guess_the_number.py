from art import logo
import random


def secret_number():
    """Chooses a secret number in ranger between 1 and 100"""
    correct_number = int(random.choice(range(1, 101)))
    
    return correct_number


def difficulty():
    """Prompt a user to choose the difficulty, set attempts accordingly and store into a variable"""
    difficulty_choice = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_choice == "easy":
        attempts = 10
    elif difficulty_choice == "hard":
        attempts = 5
    else:
        print("Okay, you've chosen ultra-hard difficulty. Good luck!")
        attempts = 1

    return attempts


def play_game():
    is_continue = True

    while is_continue:

        print("\n" * 100 + logo)

        is_playing = True

        winning_number = secret_number()

        print("Welcome to my number guessing game! Guess the number between 1 and 100 to win")

        attempts_left = difficulty()

        while is_playing:
            try:
                user_guess = int(input("Guess the number: "))
            except ValueError:
                print("Use numbers, please")
            else:
                if user_guess == winning_number:
                    is_playing = False
                    print("You win!")
                elif user_guess > winning_number:
                    attempts_left -= 1
                    print(f"Too high!\nYou have {attempts_left} attempts left!")
                else:
                    attempts_left -= 1
                    print(f"Too low!\nYou have {attempts_left} attempts left!")

            if attempts_left == 0:
                is_playing = False
                print(f"You lose! The correct number is {winning_number}")

        play_again = input("Do you want to play again? y/n ").lower()
        if play_again == 'n':
            is_continue = False
            print("Bye!")


play_game()
