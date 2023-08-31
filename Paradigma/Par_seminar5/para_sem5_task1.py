# 1. База знанаий о родственных связях

# father_of = {
#     ('John' 'Alice'),
#     ('John' 'Bob'),
#     ('Michael' 'John'),
#     ('Michael' 'Sara'),
# }

# def uncle(x,y):
#     return any((father, y) in father_of and(father, x)
#                in father_of for father in father_of
#                if (x, y)!= father)

# person_x = 'Alice'
# person_y = 'Sara'

# if uncle(person_x, person_y):
#     print(f"{person_x} - дядя {person_y}")
# else:
#     print(f"{person_x} - не дядя {person_y}")

# 2. База знаний об оценках студентов

# grades = {
#     'Alice': [9,8,7,9,9],
#     'Bob': [6,7,6,5,7],
#     'Eve': [8,9,7,8,9],
#     'Mike': [5,6,4,3,5]
# }

# def excellent_student(student):
#     return sum(grades[student]) / len(grades[student]) > 8

# def struggling_student(student):
#     return sum(grades[student]) / len(grades[student]) < 5

# students = ['Alice',
#     'Bob',
#     'Eve',
#     'Mike']

# for student in students:
#     if excellent_student(student):
#         print(f'{student} - отличник')
#     elif struggling_student(student):
#         print(f'{student} нуждается в академической помощи')
#     else:
#         print(f'{student} - средний студент')

