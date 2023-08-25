class Dog():
    def speak (self):
        return 'гав!'
    
class Cat():
    def speak (self):
        return 'мяу!'
    
class AnimalFactory:
    def create__animal(self, animal_type):
        if animal_type == 'dog':
            return Dog()
        if animal_type == 'cat':
            return Cat()
        
factory = AnimalFactory()
animal = factory.create__animal('dog')
print(animal.speak())