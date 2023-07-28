#Задача №33. Общее обсуждение
#Хакер Василий получил доступ к классному журналу и
#хочет заменить все свои минимальные оценки на
#максимальные. Напишите программу, которая
#заменяет оценки Василия, но наоборот: все
#максимальные – на минимальные.
#Input: 5 -> 1 3 3 3 4
#Output: 1 3 3 3 1


from random import randint as rd
n = int(input("Введите кол-во оценок: "))
marks= []
for i in range (n):
    marks.append(rd(1,5))
print(marks)
min_mark = min(marks)
max_mark = max(marks)
for i in range (n):
    if marks[i] == max_mark:
        marks[i] = min_mark
print(*marks)




