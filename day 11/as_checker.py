def as_checker(cards):
    for card in cards:
        if card == 11 and sum(cards) > 21:
            cards[cards.index(card)] = 1
            return cards
        else: return cards


def if_win(score1, score2):
    if score1 > 21:
        print("Its a blast, you lost!")
    elif score2 > 21:
        if score1 == 21:
            print("You won with a blackjack")
        else:
            print("Computer busted, you won")
    elif score1 > score2:
        if score1 == 21:
            print("You won with a blackjack")
        else:
            print("You won")
    elif score1 < score2:
        if score2 == 21:
            print("Computer won with a blackjack")
        else:
            print("You lost")   
    else:
        print("it's a draw")
        