                    #LOOP
my_fruits = ["banana", "apple", "melon", "orange", "cherry"]
for i in my_fruits:
    print(i) # prints all items in the list
print("=" * 50)
for i in range(len(my_fruits)):
    print(my_fruits[i])
print("=" * 50)
    #Using While LOOP
counter = 0
while counter < len(my_fruits):
    print(my_fruits[counter])
    counter += 1
print("=" * 50)

#complex loop
[print (x) for x in my_fruits]

print("=" * 50)
print ("        LIST COMPREHENSION")
print("_" * 50)
new_list = []
#appends all the items with "a" letter in their name.
for i in my_fruits:
    if "a" in i:
        new_list.append(i)
print(new_list)

#Syntax
# new_list = [expression for iten in iterable if condition ==True]
del new_list
new_list = [i for i in my_fruits if "a" in i]
new_list = ["hello" for x in my_fruits] # prints hellos instead
print(new_list)
print("=" * 50)

print("     SORTING")
print("_" * 50)
my_fruits.sort()
my_fruits.sort(reverse=True)

#sorting with a case insensitive 
my_fruits.sort(key= str.lower)

my_fruits.reverse()

print("=" * 50)
#Make a list copy
my_new_list = my_fruits.copy()
print(my_new_list )
another_list = list(my_fruits)
print(another_list )