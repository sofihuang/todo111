import car

car_1 = car.Car("Chevy","Corvette",2021,"blue")
car_2 = car.Car("Ford","Mustang",2022,"red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

# car_1.wheels = 2    car_1's wheels will be 2
# car.Car.wheels = 2  all car's wheels will be 2

print(car_1.wheels)
print(car_2.wheels)