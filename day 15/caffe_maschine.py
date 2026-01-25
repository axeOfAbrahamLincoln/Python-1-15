from data import MENU

caffe_machine = {
    'tank': {
        'water': 500,
        'milk': 500,
        'coffee': 500,
    },
    'coin slot': {
        'coins': {
            'quarters': 0.25,
            'dimes':    0.10,
            'nickels':  0.05,
            'pennies':  0.01,
        },
        'total in machine': 0.0,
    }
}


# def filling():
#     for key, value in caffe_machine.items():
#         print(f"filling the {key}...")
#         if isinstance(caffe_machine[key], dict):
#             for key2 in caffe_machine[key].keys():
#                 amount = int(input(f"filling with {key2}: "))
#                 caffe_machine[key][key2] = min(amount,1000)
#         else:
#             amount = int(input(f"fill the {key}: "))
#             caffe_machine[key] = min(amount,100)
# print(caffe_machine)  
# filling()
# print(caffe_machine)





def coffee(drink):
    return MENU[drink], MENU[drink]['cost']
def user_coins_inserted(machine):
    print("Please insert coins.")
    user_total = 0.0
    for key, value in machine['coin slot']['coins'].items():
        coins_inserted = int(input(f"How many {key}?: "))
        
        user_total += coins_inserted * value
    machine['coin slot']['total in machine'] += round(user_total,2)
    return round(user_total,2)
def update_caffemachine(machine,coffee):
    machine['coin slot']['total in machine'] = coffee['cost']
    
    




while True:
    input_drink = input("What would you like to drink? (Espresso, Latte, Cappuccino)? : ").lower()
    try:
        user_coffee, coffe_cost = coffee(input_drink)
        break
    except KeyError:
        print("Unknown drink! Please try again.")
print(user_coffee)
user_total = user_coins_inserted(caffe_machine)

print(f"Here is {user_total - coffe_cost:.2f} in change.")
update_caffemachine(caffe_machine, user_coffee)

print(f"Here is your {input_drink}! Enjoy!")
print(caffe_machine)


