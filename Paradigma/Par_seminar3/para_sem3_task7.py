class Observer:
    def update(self,message):
        pass

class ConcreteObserver(Observer):
    def update(self,message):
        print("Received message:", message)

class Subject:
    _observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self,message):
        for observer in self._observers:
            observer.update(message)

subject = Subject()

observer1=ConcreteObserver()
observer2=ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)

subject.notify('Hello, observers!')



