# Variable program
""" illegal Variable names:
4abc = 1            # Cannot start with number
abc xyz = 1         # Cannot have a space
$abc.xyz?123 = 1    # Cannot have special characters
abc-xyz = 1         # Cannot have - in the variable name
print = 1           # Cannot have a python Keywords """

""" Legal Variable names: 
abc_xyz = 1         
_abc_xyz = 1 
abcXyz123 = 1  
"""

a = 1               # Int can be 1, 0, -1
b = 5.555           # Float can be 5.555, 0.0 , -5.555
Status = True       # Boolean can be True or False

""" We can also replace the above three lines with
a, b, c = 1, 5.555, True """

print("Here is the value of a: ")
print(a)
print('Here is the value of a after float conversion: ')
print(float(a))
print('Here is the value of Status: ')
print(Status)
print("Here is the value of a: ")
print(a)

a = input("Enter a value: ")
print('Here is the value of a: ')       ## Now variable 'a' will have boolean, not integer
print(a)