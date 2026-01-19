import auction_art

print(auction_art.logo)

def highest_bidder(dictionary):
    return max(dictionary, key=dictionary.get)


is_more_bidders = True
bidders = {}

while is_more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    more_bidders = input("Are there any other bidders? Type Y or N : ")
    bidders[name] = bid
    biggest_bid = 0
    if more_bidders == "y":
        print("\n"*50)
    elif more_bidders == "n":
        # option A with biggest_bid = 0
        for key in bidders:
            if bidders[key] > biggest_bid:
                biggest_bid = bidders[key]
                winner = key

        # # option B with function and max()
        # winner = highest_bidder(bidders)
        
        print("\n"*50)
        print(f"The winner is {winner} with the bid of ${bidders[winner]}")
        is_more_bidders = False

        
    
