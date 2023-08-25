import text

def menu():
    for i, item in enumerate(text.main_menu):
        if not i:
            print(item)
        else: 
            print(f'|t{i},{item}')

    while True:
        choice = input(text.input_choice)  
        if choice.isgidit and 0<int(choice)<len(text.main_menu):
            return int(choice)  
        print(text.input_menu_error)

def print_message(msg: str):
    print