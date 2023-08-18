import random

def pyramidal_sort(list_1):
    transformation_to_pyramid(list_1)
    for i in range(len(list_1) - 1, 0, -1):
        list_1[0], list_1[i] = list_1[i], list_1[0]
        maximize_root(list_1, index=0, size=i)

def transformation_to_pyramid(list_1):
    start = ((len(list_1)- 1)-1)//2 # parent = (i-1)//2
    while start >= 0:
        maximize_root(list_1, index=start, size=len(list_1))
        start = start - 1
 
def maximize_root(list_1, index, size):
    l = index*2+1
    r = index*2+2
    if (l < size and list_1[l] > list_1[index]):
        largest = l
    else:
        largest = index
    if (r < size and list_1[r] > list_1[largest]):
        largest = r
    if (largest != index):
        list_1[largest], list_1[index] = list_1[index], list_1[largest]
        maximize_root(list_1, largest, size)
 


lst = [random.randint(1,21) for i in range (10)]
print('Unsorted list: ', end='')
print(lst)
pyramidal_sort(lst)
print('Sorted list:   ', end='')
print(lst)