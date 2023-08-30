# Функции высшего порядка:

# Создайте функцию высшего порядка,
# которая принимает другую функцию и список чисел. 
# Функция высшего порядка должна возвращать список,
# содержащий результаты применения переданной функции
# к каждому элементу списка.

def apply_function(func, numbers):
    return [func(x) for x in numbers]

def find_dividers(num):
    lst = []
    for x in range(2, 1 + num//2):
        if num % x == 0:
            lst.append(x)
    if len(lst) == 1:
        result = lst[0] 
        # если делитель один, возвращаем его          
    elif len(lst) > 1:
        result = tuple(lst)
        # если делителей несколько, возвращаем их кортежем
    else:      
        result = f'None as argument "{num}" is a prime number' 
        # если число простое, возвращаем об этом сообщение
    return result

    

#Test    
our_list = [12, 19, 25, 46, 59]
print(f'Input:\n{our_list}')
dividers = apply_function(find_dividers, our_list)
print(f'Output:\n{dividers}')


