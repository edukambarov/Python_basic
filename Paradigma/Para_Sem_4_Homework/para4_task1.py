# Чистые функции и неизменяемость данных: 

# Напишите функцию, 
# которая принимает список чисел и 
# возвращает новый список, 
# в котором каждый элемент умножен на 2.
# Убедитесь, что вы используете только чистые функции и не изменяете исходный список.

def multiply_list_with_argument(lst: list[int], arg = int) -> list[int]: #возвращает новый список 
    # result = [] #возвращает новый список    
    # for any in lst:
    #     result.append(any*arg) # в котором каждый элемент умножен на 2.
    # return result
    return [x*arg for x in lst]

#Test
from random import randint

data = [randint(1,10) for x in range(randint(5,10))]
print(f'Input:\n{data}')
multiplier = 2
modified_data = multiply_list_with_argument(data,multiplier)
print(f'Output:\n{modified_data}')
