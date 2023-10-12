# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("you start the engine")
        return self # in method chaining you must return sth to avoid provoking error
    
    def drive(self):
        print("you drive the car")
        return self
    
    def brake(self):
        print("you step on the brakes")
        return self

    def turn_off(self):
        print("you turn off the engine")

car=Car()
car.turn_on()\
   .drive()\
   .brake()\
   .turn_off()