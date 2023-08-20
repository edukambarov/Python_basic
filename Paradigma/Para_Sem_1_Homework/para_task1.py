# Императивное программирование:

# Задача 1:

# Подсчет суммы четных чисел от 1 до N. 
# Напишите программу, используя цикл,
# которая находит сумму всех четных чисел 
# в диапазоне от 1 до заданного числа N.

def sum_even_imperative(n):
    numbers = [x for x in range (1, n+1)]
    sum = 0
    for num in numbers:
        if num%2 == 0:
            sum += num           
    return sum

result = sum_even_imperative(10)
print(result)
