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

def find_max_seq(x: str, y: str):
    xx = list(x)
    yy = list(y)
    a = []
    b = []
    for any in xx:
        if any in set(yy):
            a.append(any)
    for item in yy:
        if item in set(xx):
            b.append(item)
    seq = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i:] == b[j:]:
                seq.append(a[i:])
    max_seq = seq[0]
    for k in range(1,len(seq)):
        if len(seq[k]) > len(max_seq):
            max_seq = len(seq[k])
    result = ''.join(max_seq)
    return result


X = "AGGTAB"
Y = "GXTXAYB"
print(find_max_seq(X, Y))

# Интересно, но не пригодилось:-)

# def count_letters(lst: str):
#     xlist = list(lst)
#     xcount = [None] * len(xlist)
#     for j in range(len(xlist)-1):
#         xcount[j] = xlist[:j+1].count(xlist[j])
#     xcount[-1] = xlist.count(xlist[-1])

#     xmod = []
#     for j in range(len(xlist)):
#         xmod.append(xlist[j] + str(xcount[j]))
#     return xmod
    
        
        
