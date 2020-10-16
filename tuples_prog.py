# tuples program in Python
# Initialize the elements into the tuple
# Tuples cannot be edited after created.
# You cannot add/update/remove elements from tuple.
# Only operations allowed are count() and index()
mytuple = ("Red","Blue","Violet","Green","Yellow","Orange","White", "Green")
print(mytuple)   # Printing whole tuple.

print("Printing count of element - Green: ",mytuple.count("Green"))
print("Printing the index of element - Green: ",mytuple.index("Green"))

newlist = list(mytuple)     # Convert tuple to list, so can be edited.
newlist[1] = "Black"        # Can add/edit/remove list
mytuple = tuple(newlist)    # Converting back list to tuple.

print("Edited Tuple: ",mytuple)     # Printing edited tuple.
newtuple = ("White", "Pink")        # Creating new tuple.
finaltuple = newtuple + mytuple     # Appending two tuples.
print(finaltuple)                   # Printing final tuple.
del newtuple                        # Deleting a tuple.

print(mytuple)   # Printing whole tuple.
""" Important points:
tuple element position start with 0 till n-1
When printing tuple, the range [a,b] meaning...
ath position (included) till bth position (not included) 
"""
print(mytuple[4])   # Printing element at 1 position from the tuple.
print(mytuple[-2])   # Printing element at -2 position from the tuple.
print(mytuple[1:4])   # Printing element at 1st position till 4th (not included)
print(mytuple[:4])   # Printing elements till 4th position (not included)
print(mytuple[1:])   # Printing elements starting 1st position (not included)

