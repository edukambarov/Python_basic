from random import randint


# cols = int(input("Введите кол-во столбцов (от 4 и более): "))
# rows = int(input("Введите кол-во строк (от 4 и более): "))
# maze = [[1 for _ in range(cols)] for _ in range(rows)]
# for i in range(1,rows-1):
#     for j in range(1,cols-1):
#         maze[i][j]= randint(0,1)

m = [
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1], 
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],    
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
]

for row in m:
    for element in row:
        print(element, end=' ')
    print()

path=[]
i_start = 10
j_start = 1
i_finish = 0
j_finish = 6
i_min = 0
i_max = len(m)-1
j_min = 0
j_max = len(m[0])-1
i = i_start
j = j_start
step=0
path.append((i_start,j_start))
if i_start == i_max: #вверх
    i-=1  
elif j_start == j_min: #вправо
    j+=1             
elif i_start == i_min: #вниз
    i+=1                
elif j_start == j_max: #влево
    j-=1              
if m[i][j] == 0:
    path.append((i,j))    
while not(i == i_finish and j==j_finish):
    if m[i-1][j]==0 and (i-1,j) not in path: #вверх и ни шагу назад:-)
        i-=1    
    elif m[i][j+1]==0 and (i,j+1) not in path: #вправо и ни шагу назад:-)
        j+=1     
    elif m[i+1][j]==0 and (i+1,j) not in path: #вниз и ни шагу назад:-)
        i+=1     
    elif m[i][j-1]==0 and (i,j-1) not in path: #влево и ни шагу назад:-)
        j-=1
    path.append((i,j))

print(path)




for i in range(len(m)):
    for j in range(len(m[i])):
        if (i,j) in path:
            m[i][j] = 2
for row in m:
    for element in row:
        print(element, end=' ')
    print()
    

   














     
   




   
      






