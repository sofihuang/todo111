# str.format() = optional method that gives users 
#                more control when displaying output

animal="cow"
item="moon"

print(" The "+animal+" jumped over the "+item ) # without str.format()
print(" The {} jumped over the {}".format(animal,item)) # can write "cow" ,"moon" directly
print(" The {1} jumped over the {0}".format(animal,item)) # positional argument
print(" The {one} jumped over the {two}".format(one="cow",two="moon")) # keyword argument

text = " The {} jumped over the {}"
print(text.format(animal,item))

# give some padding

name ="sophie"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))


number = 3.14159
number2= 1000

print("The number pi is {:.2f}.".format(number))
print("The number is {:,}.".format(number2))
print("The number is {:b}.".format(number2)) #binary
print("The number is {:o}.".format(number2)) #octal
print("The number is {:x}.".format(number2)) #lower case hexadecimal
print("The number is {:X}.".format(number2)) #upper case hexadecimal
print("The number is {:e}.".format(number2)) #lower case scientific notation
print("The number is {:E}.".format(number2)) #lower case scientific notation


