# Задача 26
# Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B с 
# помощью рекурсии.


def f(a,b):
    if b == 0:
        return 1
    return a * f(a, b-1)

a = int(input("Введите число a (основание): "))
b = int(input("Введите число b (степень): "))
print(f(a,b))