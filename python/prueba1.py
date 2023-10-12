name = "sophie"
print("hello "+name)
#print(type(name))

age=21
age+=1
print("you age is: "+str(age))

height = 150.4
print("your height is "+str(height))

human=False
print("are you a human: "+str(human))

print("*****************type casting***********************")

x=1
y=2.0
z="3"

x=str(x)
z=int(z)

print(x*3)
print("y is string now "+str(y))
print(z*3)

print("*********************************************")

name2,age2,human2="jenny",20,True
print(name2)
print(age2)
print(human2)

juan=susan=jack=30
print(juan)
print(susan)
print(jack)

print("*********************************************")

frase="Hello World"
print(len(frase)) #length of frase
print(frase.find("o")) #find letter's position
print(frase.capitalize()) #first letter in uppercase
print(frase.upper())
print(frase.lower())
print(frase.isdigit()) #bool
print(frase.isalpha()) #is is only letter true
print(frase.count("o")) #count letter
print(frase.replace("o","a")) #repalce o to a
print(frase*3) #print 3 times variable frase