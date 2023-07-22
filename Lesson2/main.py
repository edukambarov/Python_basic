# list_1 = []
# list_1 = list()
# list_1 = [1,2,3,8]
# print(*list_1)

# for i in list_1:
#     print(i)

# print(len(list_1))

# print(list_1[-1])

# list_1 = [1,5]
# print(list_1)
# list_1.append(8)
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) #0
# print(list_1)
# print(list_1.pop()) #21
# print(list_1)
# print(list_1.pop()) #-1
# print(list_1)

# Удаление конкретного элемента из списка

# print(list_1.pop(0)) 
# print(list_1)

# print(list_1.insert(2,11))
# print(list_1)


# list_1 = [1,2,3,4,5,6,7,8,9,10]
# print(list_1[0])               #1
# print(list_1[1])               #2
# print(list_1[len(list_1)-1])   #10
# print(list_1[-5])              #6
# print(list_1[:])               #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2])              #[1, 2]
# print(list_1[len(list_1)-2:])  #[9, 10]
# print(list_1[2:9])             #[3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18])           #[]
# print(list_1[0:len(list_1):6]) #[1, 7]
# print(list_1[::6])             #[1, 7]

# Кортежи
# t = ()
# print(type(t))
# t = (1, 5, 3, )
# print(type(t))
# v = [1, 8, 9]
# print(type(v))
# v = tuple(v)
# print(type(v))
# print(v)

# a = 1
# b = 2
# a,b = 1,2
# a = b = 1
# a,b,c = v
# print(a,b,c)

# t = (1,2,3,5,)
# print(t[1])
# for i in t:
#     print(i)
# for i in range(len(t)):
#     print(t[i])
# t[0]=2
# t = [1,2,3,5]
# t[0]=2
# print(t)

# Словари

# d = {}
# d = dict()
# d['q'] = 'qwerty'
# print(d)
# d['w'] = 'werty'
# print(d)
# print(d['q'])

# dictionary = {}
# dictionary = {'up': '↑', 'down': '↓', 'right': '→', 'left': '←'}
# # print(dictionary)
# # print(dictionary['left'])
# dictionary[895] = 98998
# print(dictionary)
# # print(dictionary['type']) #Error
# del dictionary['left'] #удаление элемента по ключу
# for item in dictionary:
#     # print(item)
#     print('{}:{}'.format(item, dictionary[item]))

# print(dictionary.items())
# for k,v in dictionary.items():
#     print(k,v)

# Множества

# colors = {'red','green','blue'}
# print(colors)
# colors.add('red') # не добавится, т.к. уже есть
# print(colors)
# colors.add('yellow')  #добавится
# print(colors)
# colors.remove('red') #удаление элемента
# print(colors)
# colors.discard('red') # поиск нужного элемента и удаление, если найдено
# print(colors)
# colors.clear() # удаление всех элементов множества
# print(colors)

# q = set() # создание пустого множества

# Операции со множествами в Python:

# a = {1,2,3,5,8}
# b = {2,5,8,13,21}
# c = a.copy()                                 #{1,2,3,5,8}
# u = a.union(b)                               #{1,2,3,5,8,13,21}
# i = a.intersection(b)                        #{2,3,5}
# dl = a.difference(b)                         #{1,3}
# dr = b.difference(a)                         #{13,21}
# q = a.union(b).difference(a.intersection(b)) #{1,8,13,21}

# a = {1, 8, 6}
# b = frozenset(a) #замороженное множество
# print(b)

# Генератор списков

# list_1 = [i for i in range(1,101)]                     # создать список чисел от 1 до 100
# list_1 = [i for i in range(1,101) if i % 2 == 0]       # создать список чётных чисел от 1 до 100
# list_1 = [(i,i) for i in range(1,101) if i % 2 == 0]   # добавить пары (кортежи)
# list_1 = [i*2 for i in range(10) if i % 2 == 0]        # применить умножение к списку
# print(list_1)                                          #[0, 4, 8, 12, 16]

# Профилирование и отладка