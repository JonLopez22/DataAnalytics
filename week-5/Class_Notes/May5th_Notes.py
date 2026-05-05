a = 5
b = 5
print(a == b)

x = 10
y = 3
print(x != y)

num1 = 7
num2 = 4
print(num1 > num2)

a = 2
b = 8
print(a < b)

x = 6
y = 6
print(x >= y)

name = "Hello"

print(f"Original string: {name}")
print(f"First character: {name[0]}")


string= "Hello, World!"
# Acessing the first character
print(string[0])  # Output: H

# Acessing the last character using negative indexing
print(string[-1])  # Output: !

# Slicing from index 1 to 4 (excluding 4)
print(string[1:4])  # Output: ell

# Concatenating
greeting = "Hello, " + "World!"
print(greeting)  # Output: Hello, World!

# Repetition
repeat = "Hello! " * 3
print(repeat)  # Output: Hello! Hello! Hello!

# Membership
print("World" in string)  # Output: True

string = "Hello, World!"

# convert to uppercase
print(string.upper())  # Output: HELLO, WORLD!

# find a substring
print(string.find("World"))  # Output: 7

#replace a substring
print(string.replace("World", "Python"))  # Output: Hello, Python!

# split a string 
print(string.split(", "))  # Output: ['Hello', 'World!']

