# Задача №35. Общее обсуждение
# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def simple_numbers(x):
#     for i in range(2,x-1):
#         if x%i !=0:
#             return 'yes'
#         return 'no'

n = int(input("Введите число: "))
# simple_numbers(n)

count_del = 0
i = 2
while count_del == 0 and i <= n/2:
    if n % i == 0:
        count_del+=1
    i+=1
print("yes" if count_del == 0 else "no")
