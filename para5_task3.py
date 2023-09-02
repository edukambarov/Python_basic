# Задача 3:

# НОП (наибольшая общая подпоследовательность) двух строк — 
# это самая длинная последовательность символов,
# которая содержится и в первой, и во второй строке, в том же порядке, 
# но не обязательно подряд. 
# Другими словами, это максимально длинная последовательность символов, 
# которая является "общей" для обеих строк.
# __
# Пример:

# makefile
# Copy code
# X = "AGGTAB"
# Y = "GXTXAYB"
# Наибольшая общая подпоследовательность: 
# "GTAB" (другие НОП также могут быть "GTTAB" и "GTXAB").

# Задача состоит в том, чтобы написать программу, 
# которая находит НОП для двух заданных строк.

def find_seq(lst1: list[str], lst2: list[str]):
    a = count_letters(lst1)
    b = count_letters(lst2)
    c = set(a).intersection(set(b))
    res = []
    for any in a:
        if any in c:
            res.append(any)
    print(res)

    # print(res)
    for any in res:
        if any.isdigit():
            res.remove(any)
    return ''.join(res)


def count_letters(lst: list[str]):
    xlist = list(lst)
    xcount = [None] * len(xlist)
    for j in range(len(xlist)-1):
        xcount[j] = xlist[:j+1].count(xlist[j])
    xcount[-1] = xlist.count(xlist[-1])
    xmod = []
    for j in range(len(xlist)):
        xmod.append(xlist[j] + str(xcount[j]))
    return xmod

x = "AGGTTAB"
print(count_letters(x))
y = "GXTXTAYB"
print(count_letters(y))
print(find_seq(x,y))
    
        
        