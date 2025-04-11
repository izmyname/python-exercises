from art import logo

print(f"{logo}\nWelcome to our secret auction!")

bidders = {}

def bid_input():
    name = input("Your name: ")
    bid = int(input("Your bid: $"))
    bidders[name] = bid


def highest_bid():
    bid = 0
    winner = ""
    for name in bidders:
        if bidders[name] > bid:
            bid = bidders[name]
            winner = name
    print(f"The winner is {winner} with the bid ${bid}.")

auction_going = True

while auction_going:
    bid_input()
    other_bidders= input("Are there any other bidders? yes/no ").lower()
    print("\n" *100)
    if other_bidders == "no":
        auction_going = False
        highest_bid()
