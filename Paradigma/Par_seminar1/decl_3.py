def filter_even_sum_sq_declarative(numbers):
    return sum([num**2 for num in numbers if num%2 ==0])

numbers = [1,2,3,4,5,6,7,8]
result = filter_even_sum_sq_declarative(numbers)
print(result)