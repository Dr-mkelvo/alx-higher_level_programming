        #Tuples
print("Tuples")
print("_" * 50)
#For any changes you must first convert the tuple into a list

my_tuple = ("me", "I", "myself") 
del my_tuple

#print(my_tuple) # will raise an error


#Unpacking tuples
fruits = ("banana", "cherry", "mango", "orange", "pineapple")
(green, blue, red, white, black) = fruits
print(green, blue, red, white, black)

cars = ("Lambo", "Limo", "Jeep", "Range")
(white, yellow, *black) = cars
print(white, yellow, black)
print("=" * 50)