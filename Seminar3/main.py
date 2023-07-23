# Задача 1. 

# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# lst = {1,2,1,1,4,5,3,-2}
# lst = len(set(lst))
# print(lst)

# import random
# print(lst := [random.randint(0,10) for _ in range(15)])
# new_list = []
# for i in lst:
#     if i not in new_list:
#         new_list.append(i)
# print(len(new_list))


# Задача 2. 
# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# n = int(input("Введите кол-во чисел в последовательности: "))
# k = int(input("Введите положительное число (смещение): "))
# import random
# array = [random.randint(1,20) for i in range (n)]
# print(array)
# result = []
# for i in range (n):
#     result = array[k:]+array[:k]
# # for i in range (n):
# #     if i+k >= n:
# #         result.append(array[i]) 
# # for j in range (n-k):
# #     result.insert(k+j,array[j])    
# print(result)

# import random
# print(lst := [random.randint(0,10) for _ in range (5)])

# shift = int(input("Введите положительное число (смещение): "))
# for i in range(len(lst)):
#     print(lst[(i-shift) % len(lst)], end=' ')

# Задача 3. 
# Напишите программу для всех уникальных значений(элементов) в словаре

# dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
# unique = set()

# dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
# unique = set(values for in_dict in dict for values in in_dict.values())
# print(unique) 

# for i in dict:
#     unique.add(str(*i.values()))
# print(unique)

# for d in dict:
#     for (i,j) in d.items():
#         unique.add(j)
# print(unique)

# Задача 4.
# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)


# import random
# print(lst := [random.randint(0,10) for _ in range (int(input("Введите размер массива: ")))])
# count = 0
# for i in range (1, len(lst)):
#     if lst[i]>lst[i-1]:
#         count+=1
# print(count)



