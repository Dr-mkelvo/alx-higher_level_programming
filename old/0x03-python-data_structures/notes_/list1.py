my_fruits = ["banana", "apple", "melon", "orange", "cherry"]
# print the length 
print(len(my_fruits))
#determine type
print(type(my_fruits))
#list() constructor
# Convert a tuple to a list
my_tuple = (True, "Me", 23, -76, 32.13)
print(list(my_tuple))
#Check if item is in a list
if "apple" in my_fruits:
    print("Yes, Apples are in the list")
#Changing Items in a list
my_fruits[2] = "grapes"
print(my_fruits)
my_fruits[2:4] = ["watermelon", "mango"]
print(my_fruits)
#Change 2 items by replacing with 1 tem
my_fruits[1:3] = ["blackcurrant"]
print(my_fruits)


#Append Items -adds at the of the list
my_fruits.append("pawpaw")

#Insert - Adds using index
my_fruits.insert(1, "pineapple")

#Concat using extend()
my_classes = ["python", "js", "c"]
my_fruits.extend(my_classes)
print(my_fruits)
# if you concat a tuple the result is a list
                #REMOVE
my_fruits.remove("banana")
print(my_fruits)
my_fruits.pop(2) #if you don't enter an index it removes the last item
print(my_fruits)
del my_classes[0]
del my_classes # removes all items 
my_letters = ["a", "b", "c", "d"]
my_letters.clear() # Empties the list