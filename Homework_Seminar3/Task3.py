# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

d = []
den1 = dict.fromkeys(['A','E','I','O','U','L','N','S','T','R'],1)
d.append(den1)
den2 = dict.fromkeys(['D', 'G'],2)
d.append(den2)
den3 = dict.fromkeys(['B','C','M','P'],3)
d.append(den3)
den4 = dict.fromkeys(['F','H','V','W','Y'],4)
d.append(den4)
den5 = dict.fromkeys(['K'],5)
d.append(den5)
den8 = dict.fromkeys(['J','X'],8)
d.append(den8)
den10 = dict.fromkeys(['Q','Z'],10)
d.append(den10)
dru1 = dict.fromkeys(['А','В','Е','И','Н','О','Р','С','Т'],1)
d.append(dru1)
dru2 = dict.fromkeys(['Д', 'К','Л','М','П','У'],2)
d.append(dru2)
dru3 = dict.fromkeys(['Б','Г','Ё','Ь','Я'],3)
d.append(dru3)
dru4 = dict.fromkeys(['Й','Ы'],4)
d.append(dru4)
dru5 = dict.fromkeys(['Ж','З','Х','Ц','Ч'],5)
d.append(dru5)
dru8 = dict.fromkeys(['Ш','Э','Ю'],8)
d.append(dru8)
dru10 = dict.fromkeys(['Ф','Щ','Ъ'],10)
d.append(dru10)
word = str(input("введите слово: ")).upper()
sum = 0
letters=list(word)
for l in letters:
    for q in d:
        for (i,j) in q.items():
            if l == i:
                sum+=j
print(sum)


    