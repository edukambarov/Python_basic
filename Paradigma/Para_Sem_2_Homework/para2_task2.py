# Процедурное программирование:
# __
# Разбиение массива на подмассивы:
# __
# Описание: 
# Имеется массив чисел. Необходимо разбить его на подмассивы так, 
# чтобы сумма чисел в каждом подмассиве была меньше или равна заданному значению X.
# Почему это процедурное программирование:
# Можно создать процедуру, которая будет принимать массив и значение X, 
# а затем последовательно формировать подмассивы, следуя определенной логике.
# Это позволяет выделить процесс создания каждого подмассива в отдельную подпрограмму,
# делая основной код более чистым и понятным.




# Задание:
# Напишите функцию, которая принимает массив чисел и значение X. 
# Функция должна возвращать массив подмассивов так, 
# чтобы сумма чисел в каждом подмассиве была меньше или равна X.
# Входные данные:
# Массив чисел длиной N.
# Число X.
# Выходные данные:
# Массив подмассивов.

from random import randint 

def segregate_by_parameter(lst, value):
    result = []
    subresult = []
    i = 0
    sum = 0
    start = 0
    for x in range(start, len(lst)):
        sum+=lst[x]
        if sum<=value:
            subresult.append(lst[x])
        else:
            result.insert(i,subresult)
            subresult = []
            subresult.append(lst[x])
            sum = lst[x]
            start = x - 1
            i+=1
    result.insert(i,subresult)
    return result

n = int(input('Введите кол-во элементов в списке: '))
m = int(input('Введите максимальное значение элемента списка: '))
init_list = [randint(1,m) for _ in range(n)]
print(f'Исходный список: {init_list}')
parameter_1 = int(input('Введите параметр (число) для сравнения и формирования вложенных списков: '))
print(f'Результат: {segregate_by_parameter(init_list,parameter_1)}')

