import time
import random

def work_time(func, x):
    start = time.time()
    func(x)
    print(f'Времени ушло {time.time()-start}')
    print()

def calc_count(sp):
    total = 0
    for item in sp:
        if isinstance(item, list):
            total = total + calc_count(item)
        else: 
            total += item
    return total

count_angola = 18
count_new_york = [20, [10, 7]]
count_chicago = 15
count_usa = [count_new_york, count_chicago]
count_all = [count_usa, count_angola]
print(count_all)
print(calc_count(count_all))

