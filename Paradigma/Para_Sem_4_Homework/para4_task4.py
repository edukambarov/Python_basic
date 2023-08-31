# Ленивые вычисления: 

# Напишите функцию, 
# которая будет генерировать бесконечную последовательность простых чисел.
# Используйте ленивые вычисления,
# чтобы генерировать только те числа, которые действительно нужны.


def prime_numbers_generator():
    a = 1
    prime_numbers = []
    prime_numbers.append(a)
    numbers = []
    numbers.append(a)
    while True:        
        yield prime_numbers
        a+=1          
        numbers.append(a)
        for x in numbers:
            for y in range(2, x): 
                if (x % y) == 0: 
                    break             
            else:
                if x not in prime_numbers:
                    prime_numbers.append(x)


prime_nums = prime_numbers_generator()
for _ in range(55):
    print(*next(prime_nums))


        