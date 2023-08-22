from random import randint


# cols = int(input("Введите кол-во столбцов (от 4 и более): "))
# rows = int(input("Введите кол-во строк (от 4 и более): "))
# maze = [[1 for _ in range(cols)] for _ in range(rows)]
# for i in range(1,rows-1):
#     for j in range(1,cols-1):
#         maze[i][j]= randint(0,1)

a = [
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
for row in a:
    for element in row:
        print(element, end=' ')
    print()




