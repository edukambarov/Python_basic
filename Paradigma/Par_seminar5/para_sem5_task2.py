# # Задача: Напишем программу, которая проверяет, является ли заданное число палиндромом.

# word = str(input('Введите слово: '))
# if word == word[::-1]:
#     print("Палиндром")
# else:
#     print("Не палиндром")

# # Сколько раз у нас встретилось каждое слово:

# str_1 = 'Python is a programming language. Python language is used for web development, data analysis, enging learning and more'
# res = list(str_1.replace(",","").replace(".","").lower().split())
# # for word in res:   
# #     print(f'{word}: {res.count(word)}')
# lib = {}
# for i in res:
#     if i in lib:
#         lib[i]+=1
#     else:
#         lib[i]=1
# lib2 = sorted(lib.items(), key = lambda item: item[1], reverse = True)
# print(lib)
# print(lib2)


# Написать программу, которая анализирует текст и
# считает наиболее встречающиеся биграммы (пары последовательных слов) в нём


# str_1 = 'За окном летний дождь, и о За окном – день.Ты, вкусный чай нальешь,Что загодя успел вскипеть…Петь песни с тобою, о звездах и о море,Мы будем ночи напролет.Сто селфи для сторис, чтоб прописать тайм-коды –Жизнь, может, кто то и прочтет…, как ни крути она пройдет.  Новых страниц листва,Новых нот – бризИ по земле молва,О нас из небылиц…Пой песни со мною, о звездах и о море,Пой, ночи напролет.Сто селфи для сторис, чтоб прописать тайм-коды –Жизнь, может, кто то и прочтет…, как ни крути она пройдет.'
# res = list(str_1.replace(",","").replace(".","").lower().split())
# lib = {}
# for i in range (len(res)-1):
#     if (res[i], res[i+1]) in lib:
#         lib[res[i], res[i+1]]+=1
#     else:
#         lib[res[i], res[i+1]]=1
# n = int(input("How many top bigramms?: "))
# lib2 = sorted(lib.items(), key = lambda item: item[1], reverse = True)
# print(lib2[:n])