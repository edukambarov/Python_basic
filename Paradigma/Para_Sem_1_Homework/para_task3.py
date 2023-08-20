# Декларативное программирование:

# Задача 3:

# Вычисление факториала числа. Напишите программу,
# которая находит факториал заданного числа N 
# с использованием рекурсии или встроенных функций.

import math

def find_factorial_declarative(n):
    return math.factorial(n)

print(find_factorial_declarative(5))

def find_factorial_recursive(n):
    if n == 1:
        return n
    else: 
        return n*find_factorial_recursive(n-1)

print(find_factorial_recursive(5))
