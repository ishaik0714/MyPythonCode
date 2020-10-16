# Dictionary program in Python

# Initialize the elements into the Dict.
# Dict is unordered, changeable and indexed.

mydict = {"ISBN": 12345, "Title": "My Dreams", "Author": "Abdul Kalam", "Price" : "$10"}
print(mydict)       # Print whole Dictionary
print(mydict["ISBN"])       # Print ISBN element Dictionary
mydict["ISBN"] = 67890       # Update ISBN element Dictionary
print(mydict["ISBN"])       # Print ISBN element Dictionary

# Printing the elements of Dictionary
print ("Elements of Dictionary : ")
for x in mydict:
  print(x)

# Printing the values of Dictionary
print ("Values of Dictionary : ")
for x in mydict.values():
  print(x)

# Printing the items of Dictionary
print ("Items of Dictionary : ")
for x, y in mydict.items():
  print(x,y)

# Adding an item in Dictionary
mydict["Year"]=1980
print(mydict)       # Print whole Dictionary

# Remove items from Dictionary
mydict.pop("Price")
print(mydict)       # Print whole Dictionary

# Delete item from Dictionary
del mydict["Year"]
print(mydict)       # Print whole Dictionary

# Copy the dictionary to another Dictionary
newdict = mydict.copy()

# Clear all items in the Dictionary
mydict.clear()
print(mydict)       # Print whole Dictionary
