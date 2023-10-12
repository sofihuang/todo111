print("****************** list ************************")

food = ["pizza","hamburger","hotdog","spaghetti"]

food[0]="sushi"

food.append("ice cream") #add an element
food.remove("spaghetti")
food.pop() #remove last element
food.insert(0,"cake") #add element in a determined position
food.sort()
food.clear()

for x in food:
    print(x)

print("****************** 2d list ************************")

drinks = ["coffee","soda","tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake","ice cream"]

food = [drinks,dinner,dessert]

print(food[1][2])

print("****************** collection : tuple ************************")

# tuple = collection which is ordered and unchangeable 
# used to group together related data

student = ("sofi",21,"female")

print(student.count("sofi"))
print(student.index("female"))

print()

for x in student:
    print(x)

if "sofi" in student:
    print("sofi is here")

print()

print("****************** collection : set ************************")

# set = collection which is unordered, unindexed and no duplicate value

utensils = {"fork","spoon","knife"}
dishes = {"bowel","plate","cup","knife"}

utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes) # add all elements in dishes to utensils

for x in utensils:
    print(x)

print()

dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)

print()

print(utensils.difference(dishes)) # print the elements that utensils has but no in dishes

print(utensils.intersection(dishes)) # print the elements which have in both

print("****************** collection : dictionary ************************")

# dictionary = a changeable , unordered collection of unique key : value pairs.
#  Fast because they use hashing , allow us to access a value quickliy

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':"Moscow"}

print(capitals["China"])
print(capitals.get('France'))
print(capitals.get('India'))
print(capitals.keys())
print(capitals.values())
print(capitals.items()) # print the entire dictionary


    
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China') #remove
#capitals.clear()

for key,value in capitals.items():
    print(key,value)