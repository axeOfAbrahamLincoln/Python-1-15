from data import MENU

caffe_machine = {
    'tank': {
        'water': 0,
        'milk': 0,
        'coffee': 0,
    },
    'coin slot': {
        'coins': {
            'quarters': {'count': 0, 'value': 0.25},
            'dimes':    {'count': 0, 'value': 0.10},
            'nickels':  {'count': 0, 'value': 0.05},
            'pennies':   {'count': 0, 'value': 0.01},
        },
        'total in machine': 0.0,
        'total user inserted':0.0
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
    return MENU[drink]
def user_coins_inserted(machine):
    print("Please insert coins.")
    machine['coin slot']['total user inserted'] = 0.0
    for key in machine['coin slot']['coins'].keys():
        coins_inserted = int(input(f"How many {key}?: "))
        coin_counter.append(coins_inserted)
        machine['coin slot']['coins'][key]['count'] = coins_inserted
        machine['coin slot']['total user inserted'] += coins_inserted * machine['coin slot']['coins'][key]['value']
    machine['coin slot']['total in machine'] += machine['coin slot']['total user inserted']

def update_caffemachine(machine,inserted_coins):
    machine['coin_slot'][]




while True:
    input_drink = input("What would you like to drink? (Espresso, Latte, Cappuccino)? : ").lower()
    try:
        user_coffee = coffee(input_drink)
        break
    except KeyError:
        print("Unknown drink! Please try again.")
coin_counter = []

user_coins_inserted(caffe_machine)

print(f"Here is {caffe_machine['coin slot']['total user inserted'] - user_coffee['cost']} in change.")


print(f"Here is your {input_drink}! Enjoy!")
print(caffe_machine)


