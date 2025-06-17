from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def apply_brake(self):
        pass


class Car(Vehicle):
    def start(self):
        print("start in car")

    def stop(self):
        print("stop in car")

    def accelerate(self):
        print("accelerate in car")

    def apply_brake(self):
        print("apply brake in car")


c = Car()
c.accelerate()


class Bike(Vehicle):
    def start(self):
        print("start in bike")

    def stop(self):
        print("stop in bike")

    def accelerate(self):
        print("accelerate in bike")

    def apply_brake(self):
        print("apply brake in bike")


b = Bike()
b.stop()