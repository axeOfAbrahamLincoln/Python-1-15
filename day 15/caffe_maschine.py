from data import MENU

caffe_machine = {
    'tank': {
        'water': 300,
        'milk': 300,
        'coffee': 300,
    },
    'coin slot': {
        'coins': {
            'quarters': 0.25,
            'dimes':    0.10,
            'nickels':  0.05,
            'pennies':  0.01,
        },
        'profit': 0.0,
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
    """Return the menu data and cost for the selected drink."""
    return MENU[drink], MENU[drink]['cost']
def user_coins_inserted(machine):
    """
    Calculate the total value of coins inserted by the user.

    Parameters
    ----------
    machine : dict
        Machine configuration dictionary containing a 'coin slot' with
        a 'coins' mapping coin names to their monetary values.

    Returns
    -------
    float
        Total amount of money inserted, rounded to two decimal places.
    """
    print("Please insert coins.")
    user_total = 0.0
    for key, value in machine['coin slot']['coins'].items():
        coins_inserted = int(input(f"How many {key}?: "))
        user_total += coins_inserted * value
    return round(user_total,2)
def report(machine,coffee):
    for key,value in coffee['ingredients'].items():
        if value > machine['tank'][key]:
            print(f"not enough {key} in tank")
            return False
    return True
def transaction():
    print(f"Here is {user_total - coffe_cost:.2f} in change.")
    caffe_machine['coin slot']['profit'] += user_total
def make_coffe():
    print(f"Here is your {input_drink}! Enjoy!")
    for item in user_coffee['ingredients']:
        caffe_machine['tank'][item] -= user_coffee['ingredients'][item]
        




while True:
    
    while True:
        input_drink = input("What would you like to drink? (Espresso, Latte, Cappuccino)? : ").lower()
        try:
            user_coffee, coffe_cost = coffee(input_drink)
            break
        except KeyError:
            print("Unknown drink! Please try again.")
    if report(caffe_machine,user_coffee):
        user_total = user_coins_inserted(caffe_machine)
        if user_total > coffe_cost:
            transaction()
            make_coffe()
        else:
            print(f"Not enough money for that drink. Here is your ${user_total}")
        
        



