# n  = input()
# print(n*2)
# print(type(n))


# print(f'{n} : 2 = {n//2} (ост. {n % 2})')
# print(f'{n} ^ 2 = {n**2}') 

# Любое условие возвращает любой тип bool 

# a = int(input('Введите 1е число: '))
# b = int(input('Введите 2е число: '))
# if (a>b):
#     print(f'Наибольшим из введённых вами чисел является число {a}.')
# elif (b>a):
#     print(f'Наибольшим из введённых вами чисел является число {b}.')
# else:
#     print("Числа равны")

# Задача 1. 
# m = int(input('Введите число m: '))
# n = int(input('Введите число n: '))
# print(f'Чтобы проехать {m} на машине, проезжающей {n} км в день, понадобится {(m//n)+1} дн.')

# Задача 3. 
# m = int(input('Введите число m: '))
# n = int(input('Введите число n: '))
# k = int(input('Введите число k: '))
# print((m + 1)//2 + (n + 1)//2 + (k + 1)//2)


# Задача 5. 
# i = int(input('Введите число i: '))
# j = int(input('Введите число j: '))
# if (i != j):
#     print(i + j - 1)
# else:
#     print ("Недостаточно данных")

# Задача 7.
# y = int(input('Введите год: '))
# if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#     print ("yes")
# else:
#     print ("no")

# a = n//100 
# b = (n - 100*a)//10
# c = n % 10
# res = a + b + c
# print(res)

# print(f'{n//6} {4*(n//6)} {n//6}')

# n = 385664

# # Введите ваше решение ниже

# if (n//100000 + (n%100000)//10000 + (n%10000)//1000 == (n%1000)//100 + (n%100)//10 + n%10):
#     print('yes')
# else:
#     print('no')


# if c%b ==0  or c%a ==0:
#     print('yes')
# else:
#     print('no')