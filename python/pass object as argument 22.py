class Car:
    color=None


def change_color(car,color):
        car.color=color
    
car1=Car()
car2=Car()
car3=Car()

change_color(car1,"red")
change_color(car2,"white")
change_color(car3,"blue")

print(car1.color)
print(car2.color)
print(car3.color)