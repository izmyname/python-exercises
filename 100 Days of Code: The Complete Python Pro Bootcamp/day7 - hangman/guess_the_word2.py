import random

word_list = ["apple", "road", "dog", "spider"]
chosen_word = random.choice(word_list)

placeholder = ""

for i in chosen_word:
    placeholder += "_"

print(chosen_word)  # debug
print(placeholder)

gameover = False
guessed_letters = []
attempts = 5


while not gameover:

    display = ""
    guess = input("Enter a letter: ")

    if guess in guessed_letters:
        print(f"You already guessed the letter {guess}")

    for i in chosen_word:
        if guess == i:
            display += i
            guessed_letters.append(i)
        elif i in guessed_letters:
            display += i
        else:
            display += "_"

    print(display)


    if not guess in chosen_word:
        attempts -= 1
        print(f"{guess} is not the correct letter. {attempts} attempts left")
        if attempts == 0:
            gameover = True
            print(f"You lose. The right word is {chosen_word}")

    if not "_" in display:
        gameover = True
        print("You win")


