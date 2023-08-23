
def interface():
    print('Здравствуйте!\n'
    'Вы находитесь в меню справочника.\n'
    
    '1 - найти запись\n'
    '2 - новая запись\n'
    '3 - редактировать запись\n'
    '4 - удалить запись\n'
    '5 - выйти из программы\n')

    while True:
        request = int(input('Выберите команду (1-5): '))
        if request not in (1,2,3,4,5):
            print('Скорректируйте ваш запрос.')
        elif request ==1:
            find_data()
        elif request ==2:
            pass
        elif request ==3:
            pass
        elif request ==4:
            pass
        elif request ==5:
            print('Всего доброго!')
            return

interface()