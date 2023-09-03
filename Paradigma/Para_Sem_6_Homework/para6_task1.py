# Бинарный поиск
# ● Контекст
# Предположим, что мы хотим найти элемент в массиве (получить 
# его индекс). Мы можем это сделать просто перебрав все элементы. 
# Но что, если массив уже отсортирован? В этом случае можно 
# использовать бинарный поиск. Принцип прост: сначала берём 
# элемент находящийся посередине и сравниваем с тем, который мы 
# хотим найти. Если центральный элемент больше нашего, 
# рассматриваем массив слева от центрального, а если больше - 
# справа и повторяем так до тех пор, пока не найдем наш элемент.
# ● Ваша задача
# Написать программу на любом языке в любой парадигме для 
# бинарного поиска. На вход подаётся целочисленный массив и 
# число. На выходе - индекс элемента или -1, в случае если искомого 
# элемента нет в массиве.

from random import randint

def merge_sort (lst: list[int]):
    if len(lst) > 1: 
        mid = len(lst)//2
        left = lst[:mid] 
        right = lst[mid:]
        merge_sort(left) 
        merge_sort(right) 
        i = j = k = 0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                lst[k] = left[i] 
                i+=1
            else: 
                lst[k] = right[j] 
                j+=1
            k+=1
        while i < len(left): 
            lst[k] = left[i] 
            i+=1
            k+=1
        while j < len(right): 
            lst[k] = right[j] 
            j+=1
            k+=1
    
def binary_search(lst: list[int], val: int):
    first = 0
    last = len(lst)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lst[mid] == val:
            index = mid
        else:
            if val<lst[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

our_list = [randint(1,20) for x in range(randint(10,15))]
print(f'Unsorted:\n {our_list}')
merge_sort(our_list)
print(f'Sorted:\n {our_list}')
n = int(input('Enter number to be searched: '))
if binary_search(our_list,n) > -1:
    print(f'Index: {binary_search(our_list,n)}')
else:
    print("Number was not found in the list.")





