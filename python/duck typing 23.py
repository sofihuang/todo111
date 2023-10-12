# the object is less important than methods or attribute
class Duck():

    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is talking")
        
class Chicken():
    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken is talking")

class Person():

    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("you catch the carrier")
        

duck=Duck()
chicken=Chicken()
person=Person()

person.catch(duck)
person.catch(chicken)