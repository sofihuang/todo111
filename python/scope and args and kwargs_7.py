# scope = the region that a variable is recognized
#   A variable is only available from inside the region it is created.
#   A global and locally scoped versions of a variable can be created.

name="sophie" # global scope (available inside and outside functions)

def display_name():
    name="tingting" # local scope (available only inside this function)
    print(name)

display_name()
print(name)

print("***********************************************************")

# *args = parameter that will pack all arguments into a tuple
#           useful so that a function can accept a vaying amount of argumrnt

def add (*args): # can be *stuff 
    sum = 0
    args = list (args)
    args[0] = 0      # tuple cannot be selected his position so we need a casting
    for i in args: 
        sum=sum+i

    return sum

print(add(1,2,3))

print("***********************************************************")

# ** kwargs = parameter that will pack all arguments into a dictionary
#             useful so that a function can accept a varying amount of keyword
#             argument

def greeting(**kwargs): # can named other name like **name etc
    #print("Hello "+kwargs['first']+" "+kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

greeting(title='Ms',first='tingting',middle='sophie',last='huang')