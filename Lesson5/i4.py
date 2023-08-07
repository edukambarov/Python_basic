# def calc1(a, b):
#     return a + b
# def calc2(a, b):
#     return a * b
# def math(op, a, b):
#     print(op(a,b))

# math(calc2, 3, 5)
# math(calc1, 3, 5)

data = [1,2,3,5,8,15,23,38]
res = list()

# for i in data:
#     if i%2==0:
#         res.append((i, i*i))
# print(res)

# def select (f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]
# res = map(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x*x), res))
# print(res)

# list_1 = [x for x in range(1,20)]
# print(list_1)
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)


# data = '12 34 35'
# data = list(map(int, data.split()))
# print(data)

# data = [12,25 ,34 ,35 ,56]
# res = list(filter(lambda x: x % 10 ==5, data))
# print(res)