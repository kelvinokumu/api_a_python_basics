from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):

    def start_engine(self):
        return "Car engine started"

mycar = Car()
print(mycar.start_engine())