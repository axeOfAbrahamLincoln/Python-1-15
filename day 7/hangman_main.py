import hangman_words, random, hangman_art

random_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)
print(random_word)

placeholder = []

for letter in range(len(random_word)):
    placeholder.append("_")
#print(*placeholder, sep=" ")

is_game_over = False
lives = 6
guessed_letters = []

while not is_game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    print("Word to guess: ", end="")
    print(*placeholder, sep=" ")
    guess = input("what is your guess?: ").lower()
        
   
  
    if guess in random_word and guess not in guessed_letters:
        count = 0
        for letter in random_word:
            if guess == letter:
                placeholder.pop(count)
                placeholder.insert(count,guess)
                count +=1
            else:
                count +=1
        print(f"{guess} is correct!")        
        print(hangman_art.stages[lives])
        #print(f"****************************{lives}/6 LIVES LEFT****************************")
        #print("Word to guess: ", end="")
        #print(*placeholder, sep=" ")
    elif guess in random_word and guess in guessed_letters:
        print("You already choose this letter")
        #print("Word to guess: ", end="")
        #print(*placeholder, sep=" ")
    elif guess not in random_word and guess in guessed_letters:
        print("You already choose this letter")
        #print("Word to guess: ", end="")
        #print(*placeholder, sep=" ")

    
    if guess not in placeholder and guess not in guessed_letters:
        lives-= 1
        print(f"{guess} is not correct!\nYou lost a life\nRemaining life: {lives}")
        print(hangman_art.stages[lives])
        #print(f"****************************{lives}/6 LIVES LEFT****************************")
        #print("Word to guess: ", end="")
        #print(*placeholder, sep=" ")
        if lives == 0:
            is_game_over = True
            print("You Lost")  
            
    guessed_letters.append(guess)     
    if "_" not in placeholder:
        is_game_over = True
        print("you win")
      


    








