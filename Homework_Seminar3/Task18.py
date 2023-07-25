list_1 = [1, 2, 3, 4, 5]
k = 6
# Введите ваше решение ниже
dmin = k
imin = 0
for i in range(len(list_1)):
    d = k - list_1[i]
    if abs(d) < dmin or d ==0:
        imin = i
        dmin = abs(d)
print(list_1[imin])


# Денис Макарцев
# Администратор
# from random import randint as rd


# n = int(input("Введите кол-во элементов: "))
# data_list = list()
# for i in range(n):
#     data_list.append(rd(-10, 10))
# print(data_list)
# x = int(input("Введите число: "))
# min_diff = abs(x - data_list[0])
# result_number = data_list[0]
# for i in range(1, n):
#     if abs(data_list[i] - x) < min_diff:
#         min_diff = abs(data_list[i] - x)
#         result_number = data_list[i]
# print(f'Максимально приближенное число к {x} равно {result_number}')