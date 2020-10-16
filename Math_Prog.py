## Math Program
a = float(input("Enter a first number: "))
b = int(input("Enter a second number: "))
num_add = a + b     # Addition Operator
num_sub = a - b     # Subtraction Operator
num_mul = a * b     # Multiplication Operator
num_div = a / b     # Division Operator
num_exp = a ** b    # Exponent Operator
num_mod = a % b    # Modulo Operator
floordiv = a // b    # Floor Division Operator

print(a+b)          # This is also correct.
print(6.5+12)       # This is also correct.

a = 4*5+6
print(a)
print('Here is the value of add: ', num_add)
print("Sum: ", num_add, "Sub:", num_sub)
print('Here is the value of sub: ', num_sub)
print('Here is the value of mul: ', num_mul)
print('Here is the value of div: ', num_div)
print('Here is the value of exponent: ', num_exp)
print('Here is the value of modulo: ', num_mod)
print('Here is the value of floor div: ', floordiv)

"""Order of Operation
( )     - Highest precidence
**      - Exponentiation
* / %   - Same precidence left to right
+ -     - Same precidence left to right    """
