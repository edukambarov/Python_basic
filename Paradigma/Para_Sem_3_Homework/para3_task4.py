# Шаблон Наблюдатель:

# Реализуйте паттерн Наблюдатель на языке Python для системы уведомлений.
# Создайте класс NotificationSystem (наблюдаемый объект), 
# который будет иметь методы 
# для добавления наблюдателей 
# и уведомления о событиях.
# Создайте несколько наблюдателей, реагирующих на уведомления

class Observer:
    def update(self,message):
        pass

class SetObserver(Observer):
    def update(self,message):
        print("Received message:", message)

class NotificationSystem:
    _observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self,message):
        for observer in self._observers:
            observer.update(message)

notification1 = NotificationSystem()
notification2 = NotificationSystem()

observer1=SetObserver()
observer2=SetObserver()

notification1.attach(observer1) #насколько я понял, не нужно применять attach к каждому экземпляру класса NotificationSystem

notification1.notify('Temparature at 9 a.m. will be +20°C, cloudy.')
notification2.notify('Temparature at 9 p.m. will be +14°C, drizzling.')