import calculator_art



def add(n1,n2):
    print(f"{n1} + {n2} =",n1+n2)
    return n1 + n2
def subtract(n1,n2):
    print(f"{n1} - {n2} =",n1-n2)
    return n1 - n2
def multiply(n1,n2):
    print(f"{n1} * {n2} =",n1*n2)
    return n1 * n2
def divide(n1,n2):
    if n2 == 0:
        return "You cant devide by zero"
    else:
        print(f"{n1} / {n2} =",round(n1/n2,2))
        return n1 / n2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

is_more_calc = True

while is_more_calc:
    print(calculator_art.logo)
    first_number = float(input("What's the first number?: "))
    is_more_calc = True
    while is_more_calc:
        print("+\n-\n*\n/\n")
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        

        for key in operations:
            if operation == key:
                operation = operations[key]
        result = round(operation(first_number,next_number),2)
        if result == "You cant devide by zero":
            print(result)
            break
        else:
            more_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
            if more_calc == "y":
                first_number = result
                continue
            else: 
                break
          

        

