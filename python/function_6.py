# function = a block of code which is executed only when it is called

def hello(name,name2,age):
    print("Hello! Have a nice day "+name+" "+name2)
    print("You are "+str(age)+" years old")

def multiply(n1,n2):
    return n1*n2

def greeting(first,middle,last):
    print("Hello "+first+ " "+middle+" "+last)
    

my_name = "Sophie"
last_name="Ting"
hello(my_name,last_name,23)

print(multiply(2,8))

print("**************** keyword argument **********************")

greeting(last="Huang",middle="ting",first="sophie")

print("**************** nested functions calls **********************")

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))