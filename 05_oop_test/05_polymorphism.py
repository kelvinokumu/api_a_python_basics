from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class ElectricCar(Vehicle):
    def start_engine(self):
        return "Electric Car started"

class Bike(Vehicle):
    def start_engine(self):
        return "Bike started"


def engine_starting(starting):
    print(starting.start_engine())

engine_starting(Car())
engine_starting(ElectricCar())
engine_starting(Bike())

