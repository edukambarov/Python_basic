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
    
init_list = [randint(1,5) for _ in range(15)]
parameter_1 = 10
print(init_list)
print(segregate_by_parameter(init_list,parameter_1))

# Ряд функций и методов Python также работают с вложенными списками.

# len(): Возвращает количество подсписков во вложенном списке.
# append(): Добавляет новый подсписок в конец вложенного списка.
# extend(): Добавляет элементы из одного списка в другой список.
# insert(): Вставляет новый подсписок на определенную позицию во вложенном списке.
# remove(): Удаляет первый подсписок во вложенном списке, который совпадает с указанным.