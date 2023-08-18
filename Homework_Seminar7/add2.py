text = "hello world"
phrases = text.lower().split()

def split_w(any):
    return [x for x in any]

symbols = [split_w(item) for item in text.lower().split()]
print(symbols)
s_backwards = []
for x in range(len(symbols)):
    s_backwards.append([])
    for y in range(len(symbols[x])):
        s_backwards[x].append(symbols[x][len(symbols[x])-y-1])
print(s_backwards)

# for x in range(len(symbols)):

#     for y in range(len(symbols[x])):
#         words_backwards.append(symbols[x][len(symbols[x])-y-1])


# print(str(words_backwards))