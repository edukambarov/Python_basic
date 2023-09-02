# Задача 1: 
# Напишите программу, которая находит все простые числа в заданном диапазоне.
# Простые числа - это числа больше 1, которые не имеют делителей, кроме 1 и самих себя. 
# Задача состоит в том, чтобы написать программу,
# которая будет находить и 
# выводить все простые числа в заданном диапазоне
# (в конце программа выводит список найденных простых чисел.)

def find_prime_numbers(min_value: int, max_value:int) -> list[int]:
    numbers = [x for x in range(min_value, max_value + 1)]
    prime_numbers = []
    for x in numbers:
        for y in range(2, x): 
            if (x % y) == 0: 
                break             
        else:
            if x not in prime_numbers:
                prime_numbers.append(x)
    return prime_numbers

print(find_prime_numbers(10,40))