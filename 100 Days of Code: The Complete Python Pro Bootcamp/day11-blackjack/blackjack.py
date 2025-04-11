from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


keep_playing = True

while keep_playing:

    print(logo)

    # Use lists to store both player and computer cards
    user_hand = []
    computer_hand = []

    def game_over():
        print(f"\nYour final hand {user_hand}, final score: {sum(user_hand)}\nComputer's final hand {computer_hand}, "
              f"final score {sum(computer_hand)}")

    def outcome():
        if sum(user_hand) > sum(computer_hand):
            game_over()
            print("You win!")
        elif sum(user_hand) == sum(computer_hand):
            game_over()
            print("It's a draw!")
        elif sum(user_hand) > 21 and sum(computer_hand) > 21:
            game_over()
            print("It's a draw!")
        else:
            game_over()
            print("You lose!")


    # Add first cards to both user and computer decks
    user_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))


    def blackjack_keep_playing():
        # Add one more card to both player and computer hands
        user_hand.append(random.choice(cards))
        computer_hand.append(random.choice(cards))

        print(f"Your cards: {user_hand}, current score: {sum(user_hand)}\nComputer's first card: {computer_hand[0]}")
        if sum(user_hand) == 21:
            game_over()
            print("You win!")
        elif sum(computer_hand) == 21:
            game_over()
            print("You lose!")
        else:
            if sum(user_hand) > 21:
                if 11 in user_hand:
                    ace_position = user_hand.index(11)
                    user_hand[ace_position] = 1
                    if sum(user_hand) > 21:
                        game_over()
                        print("You lose!")
                    else:
                        blackjack_keep_playing()
                else:
                    game_over()
                    print("You lose!")
            else:
                get_card = input("Do you want to get another card? y/n ").lower()
                if get_card == "y":
                    blackjack_keep_playing()
                else:
                    if sum(computer_hand) < 17:
                        computer_hand.append(random.choice(cards))
                        if sum(computer_hand) > 21:
                            game_over()
                            print("You win!")
                        elif sum(computer_hand) == 21:
                            game_over()
                            print("You lose!")
                        else:
                            outcome()
                    else:
                        outcome()


    blackjack_keep_playing()

    user_prompt = (input("Play again? y/n")).lower()
    if user_prompt == "n":
        keep_playing = False
        print("Goodbye!")
