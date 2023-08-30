class Human:
    pass

    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work

    def __str__(self):
        return f'Это человек {self.name}, которому {self.age} лет и который работает в {self.work}.'   

    def greetings(self):
        print(f'{self.name} приветствует вас!')


stone = Human('Стоун',39,'GB')
emil = Human('Эмиль',23,'Визирь')

# stone.greetings()
# emil.greetings()

human_list = [stone,emil]

for human in human_list:
    human.greetings()

print(stone)
print(emil.name)