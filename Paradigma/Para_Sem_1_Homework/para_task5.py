# Императивное программирование:

# Задача 5:

# Поиск простых чисел.
# Напишите программу, которая находит все простые числа
# в заданном диапазоне от 1 до N.

def find_prime_numbers_imperative(n):
    numbers = [x for x in range(1,n+1)]
    prime_numbers = []
    for x in numbers:
        for y in range(2, x): 
            if (x % y) == 0: 
                break 
        else: 
            prime_numbers.append(x)
    return set(prime_numbers)

z = int(input('Введите число: '))
print(*find_prime_numbers_imperative(z))

