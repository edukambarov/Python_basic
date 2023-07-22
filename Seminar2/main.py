# Задача 1. 
# По данному целому неотрицательному значению n вычислите !n. 
# Решите с помощью цикла while

# n = int(input('Введите число: '))
# factorial_n = 1
# i = 1
# while (i <= n): 
#     factorial_n = factorial_n * i
#     i += 1  
# print(factorial_n)


# Задача 2.
# Дано натуральное число А>1
# Определите, каким по счёту числом Фибоначчи является число А,
# т.е. n для Fibonacci(n) = A.
# Если не является числом Фибоначчи, выведите число -1.

# Решение группы

# n = int(input('Введите число: '))
# i = 2
# fib_1 = 0
# fib_2 = 1
# fib_3 = 0

# while n > fib_1:
#     fib_3 = fib_1 + fib_2
#     fib_1 = fib_2
#     fib_2 = fib_3
#     i+= 1  
#     if fib_3 == n:
#         print(i)
#         break
# else:
#     print(-1)

# Решение преподавателя

# num = int(input('Введите число: '))
# fib_prev, fib_cur = 0,1
# i = 1
# while fib_cur < num:
#     fib_prev, fib_cur = fib_cur, fib_prev + fib_cur
#     i+=1
# if fib_cur == num:
#     print(i)
# else:
#     print(-1)

# Задача 3. 

# Арбуз для себя самый тяжелый, арбуз для тёщи самый лёгкий

# import random
# n = int(input('Введите кол-во арбузов: '))
# min_w, max_w = 30, 1
# for i in range(n):
#     melon = random.randint(1, 30)
#     if min_w > melon:
#         min_w = melon
#     if max_w < melon:
#         max_w = melon
# print(min_w, max_w)

# Задача 4.

# Определить самую долгую оттепель (temp > 0) в течение месяца зимы

days = 30
temp = 0
count = 0
import random
for i in range(days):
    temp += random.randint(-10, 10)
    if temp >= 0:
        count += 1
    else: count = 0
print(f'Самая долгая оттепель составила {count} дней')