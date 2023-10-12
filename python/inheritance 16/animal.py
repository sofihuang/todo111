class Organism:

    def alivee(self):
        print("This organism is aliving")

class Animal(Organism):

    alive = True

    def eat(self):
        print("This animal is eating")
    
    def slumber(self):
        print("This animal is sleeping")


class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")
    
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")


animal_1 = Animal()

animal_1.alive
animal_1.eat()
animal_1.slumber()

rabbit = Rabbit()
rabbit.run()

fish = Fish()
fish.swim()

hawk = Hawk()
hawk.fly()

print("*********************************************************")
#multiple inheritance
fish.alivee()
fish.eat()
fish.swim()