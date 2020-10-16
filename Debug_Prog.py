# Program to demonstrate the Debugging using Pycharm.
# Swap two numbers

a = int(input("Enter the number - a: "))        # Reading integer variable "a"
b = int(input("Enter the number - b: "))          # Reading integer variable "b"
print('Here is the value of a and b: ', a, b)       # Printing the integer variable "a" and "b"

"""
temp = a
a = b
b = temp
print('After swapping with TEMP variable: ', a, b)       # Printing the integer variable "a" and "b"
"""

a = a + b       # a is a+b
b = a - b       # b is (a+b)-b = a
a = a - b       # a is (a+b)-(a+b-b) = b
print('After swapping without third variable: ', a, b)       # Printing the integer variable "a" and "b"

def swap_numbers():
    global a
    global b
    temp = int(a)   # It thinks that a is a new local variable which is not assigned to any value
    a = int(b)      # It thinks that b is a new local variable which is not assigned to any value
    b = int(temp)

if a < b:
    swap_numbers()

print("Difference between numbers is ", int(a-b))
