# higher oder function = a function either : accept a function as an argument or returns a function ( in python functions are treated as objects)

def loud(text):
        return text.upper()

def quiet(text):
        return text.lower()

def hello(func):
        text=func("Hello Sofi XD ")
        print(text)


hello(loud)
hello(quiet)

print("********************************************")
    
def divisor(x):
        def dividend(y):
                return y/x
        return dividend

divide=divisor(2)
print(divide(10))