a = int(input("Введите 1е число: "))
b = int(input("Введите 2е число: "))

import random
l = 10 #длина списка
list_1 = [random.randint(1,1000) for i in range (l)]
print(list_1)
result = []
for i in range(l):
    if a < list_1[i] < b or b < list_1[i] < a:
        result.append(i)
print(result)