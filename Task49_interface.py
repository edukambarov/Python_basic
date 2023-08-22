from Task49_handlers import find_data
from Task49_handlers import new_data
from Task49_handlers import correct_data
from Task49_handlers import new_data

def interface():
    print('Здравствуйте!\n'
    'Вы находитесь в меню справочника.\n'
    'Выберите команду (1-5):\n'
    '1 - найти запись\n'
    '2 - новая запись\n'
    '3 - редактировать запись\n'
    '4 - удалить запись\n'
    '5 - выйти из программы\n')

    while True:
        request = int(input('Введите номер команды: '))
        if request not in (1,2,3,4,5):
            print('Скорректируйте ваш запрос.')
        elif request ==1:
            find_data()
        elif request ==2:
            new_data()
        elif request ==3:
            correct_data()
        elif request ==4:
            pass
        elif request ==5:
            print('Всего доброго!')
            return

if __name__ == '__main__':
    interface()
