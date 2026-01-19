def format_name(f_name,l_name):
    full_name = (f"{f_name.title()} s{l_name.title()}")
    return full_name

first_name = input("Give me your first name:")
last_name = input("Give me your last name:")

full_name = format_name(first_name,last_name)

print(f"Your name is: {full_name}")



    