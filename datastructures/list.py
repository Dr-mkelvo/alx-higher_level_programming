thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


this = ["apple", "banana", "cherry"]
[print(x) for x in this]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "b" in x:
        newlist.append(x)
print(newlist)
