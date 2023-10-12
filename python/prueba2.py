import math

name = input("What's your name? ")
age = int(input("How old are you? "))
height = float(input("How tall are you? "))


age = age + 1

print("Hello "+name)
print("You are "+ str(age)+" years old")
print("You are "+str(height)+" cm tall")

print("***********************  math ****************************")

pi=3.14
x=1
y=2
z=3

print(round(pi)) # keep the whole number part
print(math.ceil(pi)) # round number up
print(math.floor(pi)) # round number down
print(abs(-345)) # absolut number
print(pow(pi,2)) # same as math pow in java
print(math.sqrt(420))
print(max(x,y,z)) #find the maximum number
print(min(x,y,z)) #find the minimum number

print("************************ slicing string *************************")
# slicing = create a substring by extracting elements from another string
# indexing[] or slice()
#[start:stop:step]

name = "Sophie Huang"
first_name= name[:6] # same as name[0:6]
last_name=name[7:] #same as name[7:13]
funky_name=name[::3] # same as name[0:13:3] appear each third letter
reversed_name=name[::-1] # count in reverse
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

print("************************ slice function *************************")

website="http://google.com"
website2="http://wikipedia.com"

slice=slice(7,-4)

print(website[slice])
print(website2[slice])
