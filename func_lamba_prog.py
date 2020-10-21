# Functions and Lambda program in Python
""" Function
    - Block of code which runs when called.
    - Can pass arguments.
    - Can return data.
"""
"""
def sum_func():
    print("Sum: ", a+b)

def diff_func(x,y):         # Picking the passed arguments
    if (x>y):
        print("Difference: ", x-y)
    else:
        print("Difference: ", y-x)

def mult_func(m,n):
    return m*n          # Returning the value here

def less_func(a,b):
    if (a>b):
        return True
    else:
        return False


def concat_func(p,q):
    return (p+q)

"""
def div_func(p,q):
    if q==0:
        print("Exception - Divide by zero error !")     # Checking divide by zero exception.
    else:
        print("Division: ", float(p/q))
"""
a = int(input("Enter the number - a: "))        # Reading integer variable "a"
b = int(input("Enter the number - b: "))        # Reading integer variable "b"

# Different types of functions below

sum_func()                 # passing arguments and returning value are optional
diff_func(a,b)             # passing the arguments a,b here
c = mult_func(a,b)         # Passing arguments and collecting return value in c
bool_val = int(less_func(a,b))  # True - 1, False - 0
print (bool_val)

full_name = concat_func("FirstName", "LastName")
print(full_name)

#print("Multiply: ", c)     # printing the returned value from function
#div_func(a,b)
"""
"""Types of Arguments in Functions
    -   arg         Argument ~ Required arguments in function.
    -   *args       Arguments ~ Optional tuple containing elements
    -   **kwargs    KeyWord Arguments ~ Optional dictionary containing key and value
    def function_name (args, *args, kwargs)
"""
def arg_types(arg):
    print(arg)     # arg printed
#    print(args)     # Tuple printed
#   print(kwargs)   # Dictionary printed

#arg_types(5,3,9,6,7,8, math=60, eng=30, chem=50, phy=45)


p = 1
mytuple = (4,5,6,7,8)
#mydict = {"math":60, "eng":30, "chem":50, "phy":45}
mydict = dict(math=60, eng=30, chem=50, phy=45)

arg_types(mydict)



""" Lamba 
    - Small anonymous function.
    - Can take any number of arguments
    - Can only have one expression.
    - Syntax "lambda arguments : expression"                           
"""


