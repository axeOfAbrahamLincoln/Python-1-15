ef as_checker(cards):
    for card in cards:
        if card == 11 and sum(cards) > 21:
            cards[cards.index(card)] = 1
    return cards        