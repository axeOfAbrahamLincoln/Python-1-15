# TODO1: ask user what he would like to drink
# TODO2: 

from data import MENU

caffe_machine = {
    'tank' : {
        'water' : 0,
        'milk'  : 0,
        'coffee': 0,
    },
    'coin slot' : 0,
}

def filling():
    for key in caffe_machine.keys():
        print(f"filling the {key}...")
        if isinstance(caffe_machine[key], dict):
            for key2 in caffe_machine[key].keys():
                amount = int(input(f"filling with {key2}: "))
                caffe_machine[key][key2] = min(amount,1000)
        else:
            amount = int(input(f"fill the {key}: "))
            caffe_machine[key] = min(amount,100)
        
filling()
