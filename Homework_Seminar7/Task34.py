# Задача 34:  
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и 
# “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** 
#пара-ра-рам рам-пам-папам па-ра-па-да  
#**Вывод:
#Парам пам-пам  

text  = str(input("Введите текст. \nМежду словами внутри фразы ставьте дефисы. \nВ конце фразы (строки) поставьте пробел. \n"))

phrases = text.lower().split()

def split_w(any):
    return [x for x in any]

symbols = [split_w(item) for item in phrases]

def rhythm (list_1):
    vowels = ['а','я','о','ё','у','ю','и','ы','э','е']
    vowels_set = set(vowels)
    rhythm = []
    for x in range(len(list_1)):
        rhythm.append(0)
        for y in range(len(list_1[x])):
            if list_1[x][y] in vowels_set:            
                rhythm[x]+=1
    return rhythm

print(rhythm(symbols))
print('Парам пам-пам (Yes)' if len(set(rhythm(symbols))) == 1 else 'Пам парам (No)')