def a_progression(a1, d, n):
    list_1 = [a1 + i*d for i in range(n)]
    return list_1

x = int(input("Введите первый элемент последовательности: "))
y = int(input("Введите разницу (шаг) фрифметической прогрессии: "))
z = int(input("Введите количество элементов последовательности: "))

print(*a_progression(x, y, z))





