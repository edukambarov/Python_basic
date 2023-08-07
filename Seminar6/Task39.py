# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

#  sp = [1, 5, 3, 8, 10, 2]
# print(square(sp))
# print([item**2 for item in sp])
# print(more4_square(sp))
# print([item**2 for item in sp if item > 4])
# sp.insert(0,True)
#
# del sp[0]
# print(sp)

from random import randint

count1 = int(input("Введите кол-во элементов первого массива: "))
count2 = int(input("Введите кол-во элементов второго массива: "))

list_1 = [randint(1,10) for _ in range(count1)]
list_2 = [randint(1,10) for _ in range(count2)]

print(list_1)
print(list_2)
result = []
for i in list_1:
    if i not in list_2:
        result.append(i)
print(result)
# print([i for i in list_1 if i not in list_2])