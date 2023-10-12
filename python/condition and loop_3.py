import time

age = int(input("How old are you?"))

if age >= 18:
    if age == 100:
        print("You are a century old!")
    else:
        print("You are an adult")   
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child")

print("****************** logical operator *************************")

temp = int(input("What's the temperature outside?"))


if not(temp == 0):
    temp = temp + 1
    if temp > 0 and temp <= 30:
        print(temp)
        print("The tempture is good today, go outside!")
    elif temp < 0 or temp > 30:
        print(temp)
        print("The tempture is bad today, stay inside!")

print("******************  while loop *************************")

# name = None
# while not name:
name=""

while len(name) == 0:
    name = input("Enter your name:")

print("Hello "+name)

print("******************  for loop *************************")

for i in range(10):
    print(i+1)

for i in range(50,100+1):  # if is 100 that 100 is not inclusive
    print(i)

for i in range(50,100+1,2):  # in this case count 2 by 2
    print(i)

for i in "sophie ting":
    print(i)

#count down 10 to 1 , every count take a second
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy new year!")


print("******************  nested loop (two loops) *************************")

row = int(input("How many rows?"))
colum = int(input("How many colums?"))
symbol=input("Enter a symbol to use:")

for i in range(row):
    for j in  range(colum):
        print(symbol,end="") # end , print in same line
    print()

print("****************** loop control statemente *************************")

while True:
    name = input("Enter your name: ")
    if name != "":
        break

print("*****************************************************************")

phone_number="123-456-789"

for i in phone_number:
    if i == "-":
        continue
    print(i,end="")

print("*****************************************************************")

for i in range (0,10):
    if i == 3:
        pass
    else:
        print(i)
