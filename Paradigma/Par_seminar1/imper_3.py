def filter_even_sum_sq_imperative(numbers):
    even_numbers = []
    for num in numbers:
        if num%2 == 0:
            sum_sq += num**2                
    return even_numbers

numbers = [1,2,3,4,5,6,7,8]
result= filter_even_sum_sq_imperative(numbers)
print(result)