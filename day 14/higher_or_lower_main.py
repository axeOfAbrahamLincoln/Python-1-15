import random, art, game_data

def print_score(score):
    if score == 0:
        print(f"{art.logo}")
    else:
        print(f"{art.logo}")
        print(f"You are right. Current score: {score}")

def random_dictionary(data_list):
    list = []
    list.append(random.choice(data_list))
    list.append(random.choice(data_list))
    while list[0] == list[1]:
        list[1] = random.choice(data_list)
    return list

def print_insta_user(list_to_compare):
    print(f"Compare A: {list_to_compare[0]['name']} a(n) {list_to_compare[0]['description']} from {list_to_compare[0]['country']} ")
    print(art.vs)
    print(f"Compare B: {list_to_compare[1]['name']} a(n) {list_to_compare[1]['description']} from {list_to_compare[1]['country']} ")
    
def gameplay():
    user_score = 0
    is_game_over = False
    insta_users = random_dictionary(game_data.data)
    while not is_game_over:
        print_score(user_score)
        print_insta_user(insta_users)
        user_choice = input("Who has more followers? Type 'A' or 'B' : ").lower()
        print("\n"*20)
        if user_choice == "a":
            user_choice = insta_users[0]['follower_count']
        elif user_choice == "b":
            user_choice = insta_users[1]['follower_count']
        if user_choice == max(insta_users[0]['follower_count'],insta_users[1]['follower_count']):
            insta_users.remove(insta_users[0])
            insta_users.append(random.choice(game_data.data))
            user_score += 1
        else:
            is_game_over = True
    print(f"Sorry that's wrong. Final score: {user_score}")
    print(art.gameover)

gameplay()