# Замыкание:

# Создайте функцию, которая принимает некоторое число n
# и возвращает функцию, которая прибавляет n к своему аргументу. 
# Продемонстрируйте использование этой функции-замыкания.

def add_factor(n: int):
    def inner_add(number: int):
        return number + n
    return inner_add

#Test   
add_seven = add_factor(7)
print(add_seven(5))
print(add_seven(10))