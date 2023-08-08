#пара-ра-рам рам-пам-папам па-ра-па-да

text  = str(input("Введите текст. Между словами внутри фразы ставьте дефисы. В конце фразы (строки) поставьте пробел. "))

vowels = ['а','я','о','ё','у','ю','и','ы','э','е']
vowels_set = set(vowels)

phrases = text.lower().split()

def split_w(any):
    return [x for x in any]

symbols = [split_w(item) for item in phrases]

rhythm = []
for x in range(len(symbols)):
    rhythm.append(0)
    for y in range(len(symbols[x])):
        if symbols[x][y] in vowels_set:            
            rhythm[x]+=1
print('Yes' if len(set(rhythm)) == 1 else 'No')