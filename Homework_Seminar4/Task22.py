# Задача22.
# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
a1 = int(input("Введите кол-во элементов первого множества: "))
array1 = [random.randint(-10,10) for i in range (a1)]
a2 = int(input("Введите кол-во элементов второго множества: "))
array2 = [random.randint(1,20) for i in range (a2)]
result = list(set(array1).intersection(set(array2)))
temp = result[0]
print(array1)
print(array2)
print(result) # unsorted
for j in range(len(result)):
    for i in range(1,len(result)):
        if result[i] < result[i-1]:
            temp = result[i]
            result[i]=result[i-1]
            result[i-1]=temp
print(result) # bubblesort implemented

