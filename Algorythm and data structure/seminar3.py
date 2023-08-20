class Dog:
 
    def __init__(self, name, breed = "Дворняга"):
        self.name = name
        self.breed = breed

    def __str__(self) -> str:
        return (f'Собаку зовут {self.name}, и её порода это {self.breed}')
    
    def fas(self):
        print("Гав Гав")

dog_1 = Dog("Бобик", "Коргишпиц")

print(f'{dog_1.name},{dog_1.breed}')
dog_1.fas()
print(dog_1)

dog_2 = Dog("Тузик")
print(dog_2)

# import hashlib
# print(hash("apple"))
# print(hash("apples"))
# print(hash("apple"))

class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return f'{self.data=} {self.next=} '

class LinkedList:

    def __init__(self, head=None):
        self.head = head
       
    def add_node(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_LL(self):
        current = self.head
        while current:
            print(current)
            current = current.next
        

lst = LinkedList()
lst.add_node('1')
lst.add_node('12')
lst.add_node('123')
lst.add_node('1234')
lst.print_LL()
    