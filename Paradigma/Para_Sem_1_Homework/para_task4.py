# Декларативное программирование:

# Задача 4: 

# Поиск уникальных элементов в списке.
# Напишите программу, которая создает новый список,
# содержащий только уникальные элементы из исходного списка.

from random import randint

def find_unique_elements_in_list(lst):
    return list(set(lst))

list_1 = [randint(1,10) for i in range(15)]
print(list_1)
print(find_unique_elements_in_list(list_1))
