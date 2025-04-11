import random

# A very simplified version of the hangman game.  I wrote it because of struggle with the step 3 from the day 7 of udemy 100 days of python challenge course.

possible_words = ["moon", 'forest', "android", "country", "destiny"]
chosen_word = random.choice(possible_words)

placeholder = "" # give a user a hint about how many letters there are in the word

for p in chosen_word:
    placeholder += "*"

print(placeholder)
#print(chosen_word) # for debug

game_over = False  # We used it for a while loop

guessed_letters = []  # We put here already guessed letters, so the if-elif statement additionally checks this list for them

attempts = 5

# Our game begins!

while not game_over:

    display = ""
    guess = input("Insert a letter :").lower()


    if guess in guessed_letters:
        print(f"You already guessed the letter {guess}")

    for i in chosen_word:
        if guess == i:
            display += i  # adding the correct letter in the correct order
            guessed_letters.append(i) # add guessed letter to the list of guessed letters(duh)
        elif i in guessed_letters:
            display += i # if it's not the guessed letter, but the letter already exists in the list - print it, anyway
        else:
            display += "_"
    print(display)

    # Independent if statements for win-lose life - lose checks

    if not guess in chosen_word:
        attempts -= 1
        print(f"The letter {guess} is not in the word.\n{attempts} attempts remain")
        if attempts == 0:
            game_over = True
            print(f"The correct word is {chosen_word}\nYou lose")
        else:
            print("Try again")

    if not "_" in display:
        game_over = True
        print("You win")

