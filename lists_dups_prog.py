# Program to remove duplicates from a list in Python

# Initializing the elements into the list

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
        i=i+1                   # Not doing anything on first iteration.
        print("Doing nothing!")
        continue
    elif (numlist[i-1]==numlist[i]):    # Comparing current element and previous element.
        print("Elements same at... ", i-1, i)
        print("Removing: ", numlist[i])
        str = numlist[i]
        numlist.remove(str)             # Removing the duplicate element
        i = i-1                         # Decreasing the number of iterations by one.
        n = n-1                         # Decreasing the size of list by 1
    else:
        print("Elements NOT same at... ", i-1, i)
    i = i+1                             # If elements are not same, doing nothing.

print("\n\nFinal List after removing duplicates... ", numlist)   # Printing whole list.