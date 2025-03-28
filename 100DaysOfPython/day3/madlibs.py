import random

def get_word(word_type):
    while True:
        word = input(f"Enter a {word_type}: ").strip().lower()
        if word:
            return word  # Return valid input
        print("❌ Oops! You must enter something!")


def madlibs():

    noun = get_word("noun")
    verb = get_word("verb")
    adjective = get_word("adjective")
    adverb = get_word("adverb")  # My addition


    # Calculate the score
    length_noun = len(noun)
    length_verb = len(verb)
    length_adjective = len(adjective)
    length_adverb = len(adverb)

    score = length_noun + length_verb + length_adjective + length_adverb

        
    # Randomly choose a story
    story1 = f"Today, I saw a {adjective} {noun} that decided to {adverb} {verb} all day long!"
    story2 = f"Yesterday, I ran away from {adjective} {noun} that {adverb} tried to {verb} with me!"
    story3 = f"When I was at work, a {adjective} {noun} suddenly started to {verb} {adverb}!"
    story4 = f"I read a book about {adjective} {noun}, who {adverb} {verb} during long nights!"
    story5 = f"A year ago, a {adjective} {noun} tried to {adverb} {verb} me!"

    story_list = [story1, story2, story3, story4, story5]
    final_story = random.choice(story_list)

    print("\n🎭 YOUR MADLIBS STORY 🎭")
    print(final_story +"\n")
    print(f"Your score is {score}\n")

    # save stories to a text file
    with open('madlibs_stories.txt', 'a') as f:
        f.write(final_story + "\n")

# read saved stories
with open("madlibs_stories.txt", "r") as file:
    retrieve = file.read()

    
game_over = False

while not game_over:
    madlibs()
    play_again = input("Would you like to play again or read previous stories? y/r/n ")
    if play_again == "n":
        game_over = True
    elif play_again == "r":
        game_over = True
        print(retrieve)
        
