# Императивное программирование:

# Задача 2:

#Поиск наименьшего числа в списке. 
#Напишите программу, которая находит наименьшее число
#в заданном списке с помощью цикла.

from random import randint 

def find_min_imperative(lst):
    min = lst[0]
    for x in range (lst[1], lst[len(lst)-1]):
        if x < min:
            min = x
    return min

list_1 = [randint(-20,20) for i in range (10)]
print(list_1)
result = find_min_imperative(list_1)
print(result)



            