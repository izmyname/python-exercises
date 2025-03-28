import random
import art
from game_data import data



def format_string(account):
    """Proper formatting for our game"""
    name = account['name']
    desc = account['description']
    country = account['country']

    return f"{name}, a {desc} from {country}"


def compare_followers(position_1, position_2):

    if position_1['follower_count'] > position_2['follower_count']:

        return "a"

    else:

        return "b"



def game():

    print(art.logo)

    score = 0

    game_over = False

    account_a = random.choice(data)

    while not game_over:

        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)


        print(f"Compare A: {format_string(account_a)}")
        print(art.vs)
        print(f"Against B: {format_string(account_b)}")


        higher_score = compare_followers(account_a, account_b)

        user_choice = input("Who has more followers? Choose A or B: ").lower()
        print("\n"*3)

        if user_choice == higher_score:
            account_a = account_b
            score += 1

        else:
            game_over = True
            print(art.logo)
            print(f"You lose. Your total score is {score}")


game()
