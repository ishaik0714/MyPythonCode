# Program to remove duplicates from a list in Python

# Initializing the elements into the list
"""
mylist = ["Red","Blue","Red","Violet","Green","Yellow","Blue","Pink","Black","Violet","White",
          "Orange","Violet","White","Violet","Green","Orange","Violet","White","Violet","Green"]
print("\n Printing original list: \t",mylist)   # Printing whole list.

mylist.sort()       # sorting the list
print("Printing the sorted list:  \t",mylist)   # Printing whole list.

n=0                 # Initializing the variable to count elements in list.
for str in mylist:
   n = n+1          # Counting elements in list
print("Total elements in list: ", n)

i=0                 # Initializing the variable to traverse the loop.
while i<n:
    print("\nIteration - ", i)
    if (i==0):
        i=i+1
        print("Doing nothing!")
        continue
    elif (mylist[i-1]==mylist[i]):
        print("Elements same at... ", i-1, i)
        print("Removing: ", mylist[i])
        str = mylist[i]
        mylist.remove(str)
        i = i-1
        n = n-1
    else:
        print("Elements NOT same at... ", i-1, i)
    i = i+1

print(mylist)   # Printing whole list.
"""

numlist = [1,2,3,4,1,2,3,4]

print("\n Printing original list: \t",numlist)   # Printing whole list.

numlist.sort()       # sorting the list
print("Printing the sorted list:  \t",numlist)   # Printing whole list.

n=0                 # Initializing the variable to count elements in list.
for str in numlist:
   n = n+1          # Counting elements in list
print("Total elements in list: ", n)

i=0                 # Initializing the variable to traverse the loop.
while i<n:
    print("\nIteration - ", i)
    if (i==0):
        i=i+1
        print("Doing nothing!")
        continue
    elif (numlist[i-1]==numlist[i]):
        print("Elements same at... ", i-1, i)
        print("Removing: ", numlist[i])
        str = numlist[i]
        numlist.remove(str)
        i = i-1
        n = n-1
    else:
        print("Elements NOT same at... ", i-1, i)
    i = i+1

print("\n\nFinal List after removing duplicates... ", numlist)   # Printing whole list.