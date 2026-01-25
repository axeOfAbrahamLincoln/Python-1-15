from data import MENU

caffe_machine = {
    'tank': {
        'water': 0,
        'milk': 0,
        'coffee': 0,
    },
    'coin slot': {
        'coins': {
            'quarter': {'count': 0, 'value': 0.25},
            'dime':    {'count': 0, 'value': 0.10},
            'nickel':  {'count': 0, 'value': 0.05},
            'penny':   {'count': 0, 'value': 0.01},
        },
        'total amount': 0.0
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

def iterate_dict(d, indent=0):
    for key, value in d.items():
        print(' ' * indent + str(key))
        if isinstance(value, dict):
            iterate_dict(value, indent + 2)
        else:
            print(' ' * (indent + 2) + str(value))

# iterate_dict(caffe_machine)


input_drink = input("What would you like to drink? (Espresso, Latte, Cappucciono)? :")


print("Please insert coins.")


input_q = float(input("How many quarters?: "))* 0.25
input_d = float(input("How many dimes?: "))*0.1
input_n = float(input("How many nickles?: "))*0.05
input_p = float(input("How many pennies?: "))*0.01

sum_user_coins = input_q + input_d + input_n + input_p
 
print(f"Here is {sum_user_coins - MENU[input_drink]['cost']} in change.")
print(f"Here is your {input_drink}! Enjoy!")


