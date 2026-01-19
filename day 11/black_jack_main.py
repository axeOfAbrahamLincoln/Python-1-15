import black_jack_art, random

def y_or_n(choice):
    if choice == "y":
        return True
    elif choice == "n":
        return False
    else:
        print("Wrong answer! You have to choose y or n")
        return "wrong"
def randomize(list):
    dealed_cards = []
    for i in range(2):
        dealed_cards.append(random.choice(list))
    return dealed_cards
def computer_hitting(list_of_cards, cards_dealed):
    hitting = True
    
    while hitting :
        if sum(cards_dealed) < 13:
            cards_dealed.append(random.choice(list_of_cards))
        elif sum(cards_dealed) < 21 and hitting == random.choice([True,False]):
            cards_dealed.append(random.choice(list_of_cards))
            hitting = True
        elif sum(cards_dealed) == 21:
            hitting = False
        else:
            hitting = False
    return cards_dealed    
def player_hit(list_of_cards,cards_dealed):
    want_to_hit = y_or_n(input(f"Do you want to hit another card (y) or pass (n): "))
    if want_to_hit == True:
        cards_dealed.append(random.choice(list_of_cards))
        cards_dealed = as_checker(cards_dealed)
        if sum(cards_dealed) < 21:
            print(f"Your cards are {my_cards}, current score: {sum(my_cards)}")
            print(f"Computer first card is: {comp_cards[0]}")
            return True
        else:
            return True
    else:
        return False
def as_checker(cards):
    for card in cards:
        if card == 11 and sum(cards) > 21:
            cards[cards.index(card)] = 1
    return cards        
        
#def if_win(score1, score2):
    if score1 > score2: 
        if score1 > 21:
            print("its a Blast, you lost!")
        elif score1 == 21:
            print("BlackJack, you win")
        else: print("You won")
    elif score2 > score1 and score1 > 21:
        print("its a Blast, you lost!")
    elif score2 > score1:
        if score2 > 21 and score1 == 21:
            print("Computer Busted, You won with a BlackJack")    
        elif score2 > 21:
            print("Computer Busted, you won")
        elif score2 == 21:
            print("Computer has a BlackJack, you lost")
        else: print("Computer won")
    else:
        print("its a draw")
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
def is_correct_answer():
    answer = "wrong"
    while answer == "wrong":
        answer = y_or_n(input("Do you want to play Black Jack? (y/n): "))
    return answer
cards = [11 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
want_to_play = is_correct_answer()

while want_to_play:
    
        
    my_cards = randomize(cards)
    comp_cards = randomize(cards)

    print(f"Your cards are {my_cards}, current score: {sum(my_cards)}")
    print(f"Computer first card is: {comp_cards[0]}")
    want_to_hit = True
    while want_to_hit:
        if sum(my_cards) < 13:
            want_to_hit = player_hit(cards,my_cards)
        elif sum(my_cards) < 21:
            want_to_hit = player_hit(cards,my_cards)
        elif sum(my_cards) == 21:
            want_to_hit = False
        else:
            want_to_hit = False

    your_score = sum(my_cards)
    comp_score = sum(computer_hitting(cards,comp_cards))
    print(f"Your cards are: {my_cards}. Your final score is: {your_score} ")
    print(f"Computer cards are: {comp_cards}. Computer final score is: {comp_score}")
    if_win(your_score,comp_score)
    want_to_play = is_correct_answer()
        


