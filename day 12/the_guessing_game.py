import random, the_guessing_game_art

def dificulty(level):
    while level != True:
        answer = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if answer == "easy":
            level = True
            return 10
        elif answer == "hard":
            level = True
            return 5
        else:
            print("Wrong answer.")
            
def gameplay(guessing):
    while guessing != 0:
        print(f"You have {guessing} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        guessing -= 1
        if guessing == 0 and user_guess != number_to_guess:
            print(f"You have run out of guesses.\n {the_guessing_game_art.game_over}")
        elif user_guess == number_to_guess:
            print(f"You got it. The answer was {number_to_guess}")
            guessing = 0
        elif user_guess > number_to_guess:
            print("Too high.\nGuess again.")
            
        else: 
            print("Too low.\nGuess again")
              
print(the_guessing_game_art.logo)
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
number_to_guess = random.randint(1,100)
print(number_to_guess)
difficulty_level = False
attempts = dificulty(difficulty_level)
gameplay(attempts)








