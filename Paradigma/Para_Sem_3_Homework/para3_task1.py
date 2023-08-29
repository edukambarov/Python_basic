# Императивная vs Декларативная парадигма:

# Опишите задачу на Python, решение которой может быть представлено
# как императивное решение и
# как декларативное решение. 
# Объясните, в чем различие между двумя подходами
# и какой из них предпочтительнее в данном случае.


# Задача:

# Найти (указать) индекс числа и само число в последовательности,
# которое равно или ближе остальных по значению к заданному параметру.

# Output:
# Число: 8, индекс: 5.

from random import randint
import math

'''
Блок с вводом данных от пользователя 
для создания списка и параметра для сравнения будет одинакым
'''
min_value = int(input('Введите минимальное значение последовательности: '))
max_value = int(input('Введите максимальное значение последовательности: '))
length_of_list = int(input('Задайте длину последовательности: '))
parameter = int(input('Задайте параметр(число) для сравнения: '))

# Императивный подход

our_list = [randint(min_value, max_value) for i in range (length_of_list)]
print(our_list)
diff =[]
for i in range(len(our_list)):
    diff.append(abs(our_list[i] - parameter))
for x in range(len(diff)):
    if diff[x] == min(diff):
        print(f'Число: {our_list[x]}, индекс: {x}.')

# Декларативный подход

our_list = [randint(min_value, max_value) for i in range (length_of_list)]
print(our_list)
min_idxs = [idx for idx, val in enumerate(our_list) if val == min([abs(our_list[i] - parameter) for i in range(len(our_list))])]
for x in min_idxs:
    print(f'Число: {our_list[x]}, индекс: {x}.')

# Плюсы:
# В данном случае очень сложно выделить плюсы.
# Разве, что в одну строку можно получить список искомых индексов или значений.
# Допускаю, что это может быть важно в каких-то случаях.

# Недостатки:
# 1. Сложная конструкция: Легко ошибиться в написании, сложно находить ошибки.
# 2. Создание доп.массива min_idxs

# Вывод:
# В данном случае проще, нагляднее применять императивный подход.


