from random import randint 
import time

def perebor(x):
    start = time.time()
    for i in range(upper+1):
        if i == x:
            break
    fin = time.time()
    print(f'Число отгадано и это {i} за {i} итераций')
    print(f'Времени ушло {fin-start}')

def random_guess(x):
    start = time.time()
    k = 1
    num = randint(0, upper)
    while x != num:
        num = randint(0, upper)
        k+=1
    fin = time.time()
    print(f'Число отгадано и это {num} за {k} итераций')
    print(f'Времени ушло {fin-start}')

# def smart_guess(x):
#     start = time.time()
#     k = 1
#     num = randint(0, upper)
#     s = {num}
#     while x != num:
#         while num in s:
#             num = randint(0, upper)
#         s.add(num)
#         k+=1
#     fin = time.time()
#     print(f'Число отгадано и это {num} за {k} итераций')
#     print(f'Времени ушло {fin-start}')

def from_list(x):
    start = time.time()
    k = 0
    sp = [x for x in range(upper+1)]
    a = None
    while a != x:
        index = randint(0, len(sp)-1)
        a = sp.pop(index)
        k+=1
    fin = time.time()
    print(f'Число отгадано и это {a} за {k} итераций')
    print(f'Времени ушло {fin-start}')

def binary_search(x):
    k = 0
    start = time.time()
    left = 0
    right = upper
    current = round((right + left) /2 )
    while current != x:
        if current < x:
            left = current + 1
        else: 
            right = current - 1
        current = round((right + left) /2 )
        k+=1
    fin = time.time()
    print(f'Число отгадано и это {current} за {k} итераций')
    print(f'Времени ушло {fin-start}')

upper = 10000
x = randint(0,upper)
perebor(x)
print()
random_guess(x)
#print()
#smart_guess(x)
print()
from_list(x)
print()
binary_search(x)



import math  

def dice (k, n):
    start = time.time()
    dice = round(math.factorial(n+k-1)/(math.factorial(k)*math.factorial(n-1)))
    fin = time.time()
    print(f'Существует {dice} уникальных комбинаций для {k} игральных кубиков')
    print(f'Времени ушло {fin-start}')

k = 2
n = 6
print()
dice(k, n)

def prime_numbers(n):
    res = [i for i in range(n+1)]
    res[1] = 0
    i = 2
    while i <= round(n**0.5):
        if res[i] != 0:
            j = i**2
            while j <= n:
                res[j] = 0
                j+=i
        i+=1
    res = [i for i in res if res[i]!= 0]
    return res

n = int(input("Введите число: "))
print()
print(*prime_numbers(n))