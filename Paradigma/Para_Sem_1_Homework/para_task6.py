# Императивное программирование:

# Задача 6:

# Упорядочивание списка.
# Напишите программу, которая сортирует список чисел в порядке возрастания 
# с использованием пузырьковой сортировки или другого метода сортировки.

from random import randint

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

list_1 = [randint(-20,20) for i in range (10)]
print(list_1)
result = bubble_sort(list_1)
print(result)