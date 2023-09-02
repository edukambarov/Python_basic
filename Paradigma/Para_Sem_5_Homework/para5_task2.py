# Задача 2:

# Напишите программу, которая сортирует список чисел методом сортировки слиянием.

# Сортировка слиянием - это эффективный алгоритм сортировки,
# который разбивает список на две половины, сортирует их отдельно,
# а затем объединяет в отсортированный список.
# Задача состоит в том, чтобы написать программу,
# которая будет сортировать список чисел методом сортировки слиянием.

# Пример решения:

# Программа принимает на вход список чисел, который нужно отсортировать.
# Если список состоит из одного элемента или пуст, он считается уже отсортированным.
# В противном случае список разделяется на две половины.
# Рекурсивно вызывается сортировка слиянием для каждой половины.
# Затем отсортированные половины сливаются в один отсортированный список.
# Конечный отсортированный список возвращается.

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
    

from random import randint
our_list = [randint(1,10) for x in range(randint(5,10))]
print(f'Input:\n {our_list}')
merge_sort(our_list)
print(f'Output:\n {our_list}')