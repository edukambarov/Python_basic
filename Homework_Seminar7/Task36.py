# Задача 36:
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, 
# как, например, у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def bin_act_1 (a, b): #сложение
    return a + b

def bin_act_2 (a, b): #вычитание
    return a - b

def bin_act_3 (a, b): #умножение
    return a * b

def bin_act_4 (a, b): #возведение в степень
    return a ** b

def bin_act_5 (a, b): #целочисленное деление
    return a // b

def bin_act_6 (a, b): #остаток от деления
    return a % b

def print_operation_table(operation, a, b):
    temp = a
    if a < b:
        a = b
        b = temp   
    res = [[operation(x,y) for x in range(1,a+1)] for y in range(1,a+1)]   
    for i in range (a):
        print(*res[i], sep = '      ')
 
num_rows = int(input("Введите число: "))
num_columns =num_rows
print_operation_table(bin_act_3,num_rows,num_columns)




