import random
import math
import time

#1 Пирамидальная сортировка

def pyramidal_sort(list_1):
    transformation_to_pyramid(list_1)
    for i in range(len(list_1) - 1, 0, -1):
        list_1[0], list_1[i] = list_1[i], list_1[0]
        maximize_root(list_1, index=0, size=i)

def transformation_to_pyramid(list_1):
    start = ((len(list_1)- 1)-1)//2 # родитель = (i-1)//2
    while start >= 0:
        maximize_root(list_1, index=start, size=len(list_1))
        start = start - 1
 
def maximize_root(list_1, index, size):
    l = index*2+1
    r = index*2+2
    if (l < size and list_1[l] > list_1[index]):
        largest = l
    else:
        largest = index
    if (r < size and list_1[r] > list_1[largest]):
        largest = r
    if (largest != index):
        list_1[largest], list_1[index] = list_1[index], list_1[largest]
        maximize_root(list_1, largest, size)

print('_'*50)
print('Пирамидальная сортировка')
lst = [random.randint(1,21) for i in range (10)]
print('Unsorted list: ', end='')
print(lst)
pyramidal_sort(lst)
print('Sorted list:   ', end='')
print(lst)
print('_'*50)

#2 Сортировка подсчетом (для отрицательных чисел, со смещением)

def counting_sort_shifted(sp):
    max_item = max(sp)
    if min(sp)<0:
        shift = abs(min(sp))
    else:
        shift = 0
    lst = [0 for _ in range(max_item + shift + 1)]
    for i in sp:
        lst[i+shift] = lst[i+shift] + 1  
    res_sp = []
    for i in range(len(lst)):
        if lst[i]:
            res_sp.extend([i-shift] * lst[i])
    return res_sp
    

list_1 = [random.randint(-5,5) for i in range (10)]
print('Сортировка подсчётом')
print('Unsorted list: ', end='')
print(list_1)
print('Sorted list:   ', end='')
print(counting_sort_shifted(list_1))
print('_'*50)

#3 имитация БД по хранению чисел.

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = list(filter(lambda x: x < pivot, lst))
    center = [i for i in lst if i == pivot]
    right = list(filter(lambda x: x > pivot, lst))
    return quick_sort(left) + center + quick_sort(right)
    
def sort_choice(func1, func2, lst):                                    #шаг 2
    start = time.time()
    if len(lst) > 3*len(set(lst)): # для однородных данных, с часто повторяющимся результатом (например, температура больных в больнице)
        return func1(lst)         
    else:         
        return func2(lst)  
    
def binary_search(in_list: list, value: int):
    left = 0
    right = len(in_list) - 1
    current = (right + left) // 2
    while in_list[current] != value:
        if right < left:
            return None
        if in_list[current] < value:
            left = current + 1
        else:
            right = current - 1
        current = (right + left) // 2
    return current


list_2 = [random.randint(35,42) for i in range (random.randint(20,30))]
print('Исходный список: ')
print(list_2)                                                          #шаг 1

d_position = {i:list_2[i] for i in range (0, len(list_2),1)}           #шаг 3 

start = time.time()
list_sorted=sort_choice(counting_sort_shifted,quick_sort,list_2) 
print('Отсортированный список: ')                                      #шаг 3
print(list_sorted)
print(f'Выполнение сортировки заняло {time.time() - start} сек.')  

m = int(input('Введите число для поиска среди значений: '))            #шаг 4
start = time.time()
print(binary_search(list_sorted,m))
print(f'Бинарный поиск занял {time.time() - start} сек.')

n = int(input('Введите число для поиска изначальных индексов: '))      #шаг 5
filter_result = list(filter(lambda k: d_position[k] == n, d_position.keys())) 
print(*filter_result)
print('_'*50)