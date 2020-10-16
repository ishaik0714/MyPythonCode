mult_str  = """This is a multi line string,
this can have data in multiple lines
and can be printed in multiple lines !"""

print(mult_str)     # The Multi-line string can be in either in three single quotes or three double quotes.
st1 = "Hello"
st2 = "World!"

print (st1+st2) # String Concatenation

str1 = "Hello World!"   # Character position in a String start from 0
print("Character at position - 0 of the string: ",str1[0])  # First Character is 0
print("Sub-string from position 3 to 5: ", str1[2:5])     # 2:5 means characters at position 3rd, 4th and 5th
print("Sub-string from position -6 to -3 from end: ",str1[-6:-3])  # Negative number means, start counting from the end of string starting with 0
print("String length: ",len(str1))    # Get the string length
print("String remove whitespace: ",str1.strip())    # Remove white spaces in string
print("String to lower case: ",str1.lower())    # change the string to lower case
print("String to upper case: ",str1.upper())    # change the string to upper case
print("String to upper case: ",str1.replace('H','M'))    # Replace H with M
print("String to upper case: ",str1.split(','))    # change the string to upper case


987654321
HELLOWORD
012345678

[3:6] =
[-4:-1] =