class Animal:
    def eat(self):
        print("this animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("I'm eating a carrot")
        # it will implements a closer method

rabbit=Rabbit()
rabbit.eat()