phone_book ={}
PATH = 'phones.txt'

def open_file():
    global phone_book
    with open(PATH, 'r', encoding = 'unt-8') as file:
        data = file.readlines()
    for contact in enumerate(data,1):
        contact = contact.strip().s