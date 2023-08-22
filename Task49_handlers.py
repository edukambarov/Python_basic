def find_data():
    print('Введите Введите имя файла: ')
    file_name = input()
    data = open(file_name + '.txt','r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()

def new_data():
    print('Введите название нового файла: ')
    new_file_name = str(input())
    data = open(new_file_name + '.txt','w', encoding='utf-8')
    print('Введите ФИО и номер телефона(+7) через пробел: ')
    human_data = input()
    data.write(human_data)
    data.close()
    
def correct_data():
    print('Введите имя файла: ')
    file_name = input()
    data = open(file_name + '.txt','r', encoding='utf-8')
    # for line in data:
    #     print(line)
    print(data.read())
    data.close()
    data = open(file_name + '.txt','w', encoding='utf-8')
    print('Введите новые ФИО и номер телефона(+7) через пробел: ')
    human_data = input()
    data.write(human_data)
    data.close()

def 