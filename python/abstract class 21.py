# prevents a user from createing an object of that class
# compels a user to override abstract mehods in a child class 
# abstract class = a class whisch contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you drive a car")

    def stop(self):
        print("this car is stopp")

class Motocycle(Vehicle):
    def go(self):
        print("you drive a motocycle")
    
    def stop(self):
        print("this motocycle is stopp")

car=Car()
moto=Motocycle()


car.go()
moto.go()

car.stop()
moto.stop()