# Lists program in Python

# Initialize the elements into the list
mylist = ["Red","Blue","Violet","Green","Yellow","Orange","White"]
print(mylist)   # Printing whole list.

""" Important points:
List element position start with 0 till n-1
When printing list, the range [a,b] meaning...
ath position (included) till bth position (not included) 
"""

print(mylist[4])   # Printing element at 1 position from the list.
print(mylist[-2])   # Printing element at -2 position from the list.
print(mylist[1:4])   # Printing element at 1st position till 4th (not included)
print(mylist[:4])   # Printing elements till 4th position (not included)
print(mylist[1:])   # Printing elements starting 1st position (not included)

mylist[0] = 'Black'     # update the element at position 0
print(mylist)   # Printing whole list.
mylist.append('Red')    # Adding the element at the end.
print(mylist)   # Printing whole list.
mylist.insert(2,'Pink')    # Adding the element at position 2.
print(mylist)   # Printing whole list.
mylist.sort()
print("Sorted List: ", mylist)
mylist.reverse()
print("Reverse List: ", mylist)

mylist.remove('Red')    # Remove the element 'Red' from list.
print(mylist)   # Printing whole list.
mylist.pop()    # Remove the last element from list.
print(mylist)   # Printing whole list.
del mylist[0]   # Deleting the element in the 0th position
print(mylist)   # Printing whole list.

newlist = mylist.copy()     # Copy the list to another list.
print(newlist)   # Printing whole list.
mylist.clear()
print(mylist)   # Printing whole list.
mylist.append('Red')    # Adding the element at the end.
print(mylist)   # Printing whole list.
mylist.insert(5,'Pink')    # Adding the element at position 2.
print(mylist)   # Printing whole list.

finallist = newlist + mylist
print(finallist)
