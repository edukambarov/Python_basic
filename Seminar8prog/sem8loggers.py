phonebook = []

def menu():
    print('Здравствуйте!\n'
    'Вы находитесь в меню справочника.\n'    
    '1 - найти запись\n'
    '2 - новая запись\n'
    '3 - редактировать запись\n'
    '4 - удалить запись\n'
    '5 - выйти из программы\n')
    choice = int(input('Выберите команду (1-5):'))
    match choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            return





def open_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    for contact in data:        
        contact = contact.strip().split(';')
        phonebook.append({'name': contact[0].lower(),
                         'phone':contact[1].lower(),
                         'comment': contact[2].lower()})

def print_book(book: list):
    for contact in book:
        cont = f'{contact["name"]} {contact["phone"]} {contact["comment"]}'
        print(cont)

def find_contact(word: str):
    global phonebook
    result = []
    for contact in phonebook:
        for field in contact.values():
            if word in field:
                result.append(contact)
                break
            # else: 
            #     result.append("Увы по вашему запросу ничего не найдено.")
    return result
  
def save_file(path):
    global phonebook
    result = []
    for contact in phonebook:
        cont = ';'.join(contact.values())
        result.append(cont)
    print(result)


def add_contact(new):
    global phonebook
    phonebook.append({'name': new[0],
                    'phone': new[1],
                    'comment': new[2]})


open_file('D:\GeekBrains\Python курс Analyst\Seminar8prog\phonebook.txt')
# search = input('Введите ключевое слово для поиска: ')
# result = find_contact(search.lower())
# print_book(result)
print_book(phonebook)


# def find_data():
#     print('Введите Введите имя файла: ')
#     file_name = input()
#     data = open(file_name + '.txt','r', encoding='utf-8')
#     for line in data:
#         print(line)
#     data.close()

def find_data():
    print('Введите ключевое слово для поиска: ')
    search= input()
    result = []
    data = open('D:\GeekBrains\Python курс Analyst\Seminar8prog\phonebook.txt','r', encoding='utf-8')
    for row in data:
        for field in row:
            if search in field:
                result.append(row)
                break
    print(*result)
    data.close()

# def new_data():
#     print('Введите название нового файла: ')
#     new_file_name = str(input())
#     data = open(new_file_name + '.txt','w', encoding='utf-8')
#     print('Введите ФИО и номер телефона(+7) через пробел: ')
#     human_data = input()
#     data.write(human_data)
#     data.close()
    
# def correct_data():
#     print('Введите имя файла: ')
#     file_name = input()
#     data = open(file_name + '.txt','r', encoding='utf-8')
#     # for line in data:
#     #     print(line)
#     print(data.read())
#     data.close()
#     data = open(file_name + '.txt','w', encoding='utf-8')
#     print('Введите новые ФИО и номер телефона(+7) через пробел: ')
#     human_data = input()
#     data.write(human_data)
#     data.close()
