# Задача 1. 

# Дан список чисел.
# Опеределите, сколько в нём различных чисел.

# lst = {1,2,1,1,4,5,3,-2}
# lst = len(set(lst))
# print(lst)

# import random
# print(lst := [random.randint(0,10) for _ in range(15)])
# new_list = []
# for i in lst:
#     if i not in new_list:
#         new_list.append(i)
# print(len(new_list))


# Задача 2. 
# Дана последовательность из n целых чисел
# и положительное число k.
# Необходимо сдвинуть всю последовательность на k элементов вправо.

n = int(input("Введите кол-во чисел в последовательности: "))
k = int(input("Введите положительное число (смещение): "))
import random
array = [random.randint(1,20) for i in range (n)]
print(array)
result = []
for i in range (n):
    if i+k >= n:
        result.append(array[i]) 
for j in range (n-k):
    result.insert(k+j,array[j])    
print(result)


