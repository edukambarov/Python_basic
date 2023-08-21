from random import randint

def count_if (lst, n):
    count = 0
    for x in lst:
        if x == n:
            count+=1
    return count

list_1 = [1,1,1,0,0,2,2,3,3,3,3]
a = 3
print(count_if(list_1,a))


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

list_1 = [randint(-20,20) for i in range (10)]
print(list_1)
result = bubble_sort(list_1)
print(result)